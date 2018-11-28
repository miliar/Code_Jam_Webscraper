#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

class union_find
{
public:
	int id[2005], sz[2005];
	int size;
	union_find(int n)
	{
		size = n;
		for(int i = 0; i < n; i++)
		{
			id[i] = i;
			sz[i] = 1;
		}
	}

	int root(int i)
	{
		while(i != id[i])
		{
			id[i] = id[id[i]];
			i = id[i];
		}
		return i;
	}

	int find(int p, int q)
	{
		return root(p)==root(q);
	}

	void unite(int p, int q)
	{
		int i = root(p);
		int j = root(q);

		if(sz[i] < sz[j])
		{
			id[i] = j;
			sz[j] += sz[i];
		}
		else
		{
			id[j] = i;
			sz[i] += sz[j];
		}
	}
};

int vcb(vector<pair<int,int> > edges, int size)
{
	union_find connected(size);
	int skipped = 0;
	for(auto edge : edges)
	{
		if(!connected.find(edge.first, edge.second))
		{
			connected.unite(edge.first, edge.second);
		}
		else
		{
			skipped++;
			cerr << edge.first << " " << edge.second << endl;
		}
	}
	cerr << endl;
	return skipped;
}


//copied from https://sites.google.com/site/indy256/algo_cpp/hopcroft_karp

const int MAXN1 = 3000;
const int MAXN2 = 3000;
const int MAXM = 15000;

int n1, n2, edges, last[MAXN1], pre[MAXM], head[MAXM];
int matching[MAXN2], dist[MAXN1], Q[MAXN1];
bool used[MAXN1], vis[MAXN1];

void init(int _n1, int _n2) {
    n1 = _n1;
    n2 = _n2;
    edges = 0;
    fill(last, last + n1, -1);
}

void addEdge(int u, int v) {
    head[edges] = v;
    pre[edges] = last[u];
    last[u] = edges++;
}

void bfs() {
    fill(dist, dist + n1, -1);
    int sizeQ = 0;
    for (int u = 0; u < n1; ++u) {
        if (!used[u]) {
            Q[sizeQ++] = u;
            dist[u] = 0;
        }
    }
    for (int i = 0; i < sizeQ; i++) {
        int u1 = Q[i];
        for (int e = last[u1]; e >= 0; e = pre[e]) {
            int u2 = matching[head[e]];
            if (u2 >= 0 && dist[u2] < 0) {
                dist[u2] = dist[u1] + 1;
                Q[sizeQ++] = u2;
            }
        }
    }
}

bool dfs(int u1) {
    vis[u1] = true;
    for (int e = last[u1]; e >= 0; e = pre[e]) {
        int v = head[e];
        int u2 = matching[v];
        if (u2 < 0 || !vis[u2] && dist[u2] == dist[u1] + 1 && dfs(u2)) {
            matching[v] = u1;
            used[u1] = true;
            return true;
        }
    }
    return false;
}

int maxMatching() {
    fill(used, used + n1, false);
    fill(matching, matching + n2, -1);
    for (int res = 0;;) {
        bfs();
        fill(vis, vis + n1, false);
        int f = 0;
        for (int u = 0; u < n1; ++u)
            if (!used[u] && dfs(u))
                ++f;
        if (!f)
            return res;
        res += f;
    }
}

int totalUnused()
{
	int acc = 0;
	for(int i = 0; i < n1; i++)
	{
		if(!used[i]) acc++;
	}
	for(int i = 0; i < n2; i++)
	{
		if(matching[i] == -1) acc++;
	}
	return acc;
}


int main()
{
	int n;
	cin >> n;
	string s, f, t;
	//getline(cin,t);
	for(int i = 1; i <= n; i++)
	{
		int k;
		cin >> k;
		//cout << k << endl;
		getline(cin, t);
		vector<pair<int,int> > edges;
		map<string,int> words, swords;
		int fid = 0, sid = 0;
		for(int j = 0; j < k; j++)
		{
			cin >> s >> f;
			//cout << s << " " << f << endl;
			if(words.find(f) == words.end())
			{
				words[f] = fid;
				fid++;
			}
			if(swords.find(s) == swords.end())
			{
				swords[s] = sid;
				sid++;
			}
			//cerr << words[f] << " " << f <<endl;
			//cerr << swords[s] << " " << s <<endl;
			edges.push_back(make_pair(swords[s],words[f]));
		}
		init(sid,fid);
		for(auto edge : edges)
		{
			addEdge(edge.first, edge.second);
		}
		//int num_needed = vcb(edges, uid);

		cout << "Case #" << i << ": " << k - maxMatching() - totalUnused();
		cout << endl;
	}
	return 0;
}