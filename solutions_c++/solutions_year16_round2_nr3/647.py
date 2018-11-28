#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000+10;

bool mark[MAXN];
int n;
int match_l[MAXN],match_r[MAXN];
vector<int> adj[MAXN];

bool dfs (int v){
	if (v == -1)
		return true;
	if (mark[v] == true)
		return false;
	mark[v] = true;
	for (int i=0; i<(int)adj[v].size(); i++){
		int temp = adj[v][i];
		if (dfs(match_r[temp]) == true){
			match_l[v] = temp;
			match_r[temp] = v;
			return true;
		}
	}
	return false;
}

void main2(){
	int n; cin >> n;
	map<string,int> l,r;
	vector < pair<string,string> > q;
	int cnt_l=0,cnt_r=0;
	for (int i=0; i<n; i++){
		string a,b; cin >> a >> b;
		q.push_back(make_pair(a,b));
		if (l.find(a) == l.end())
			l[a] = cnt_l++;
		if (r.find(b) == r.end())
			r[b] = cnt_r++;
	}
	for (int i=0; i<cnt_l; i++)
		adj[i].clear();
	for (int i=0; i<(int)q.size(); i++){
		int u = l[q[i].first];
		int v = r[q[i].second];
		adj[u].push_back(v);
	}
	for (int i=0; i<cnt_l; i++)
		match_l[i] = -1;
	for (int i=0; i<cnt_r; i++)
		match_r[i] = -1;
	int res=0;
	memset(mark,0,sizeof mark);
	for (int i=0; i<cnt_l; i++) if (match_l[i] == -1){
		res+= dfs(i);
		memset(mark, 0, sizeof mark);
	}
	res+= cnt_l + cnt_r - 2*res;
	cout << n-res << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
