#include<queue>
#include<map>
#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;
typedef vector<int> VI;

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(),i##_end=(c).end();i!=i##_end;++i)
#define eprintf(s...) fprintf(stderr, s)

template<class T> inline void amin(T &a, const T &b) { if (b<a) a=b; }
template<class T> inline void amax(T &a, const T &b) { if (a<b) a=b; }
string concat(const vector<string>&v) {
    string s;
    for (int i=0; i<int(v.size()); i++) s += v[i];
    return s;
}
vector<string> split(const string&s, char c=' ') {
    int p=0;
    vector<string>ret;
    for (int i=0; i<int(s.size()); i++) {
	if (s[i]==c) {
	    ret.push_back(s.substr(p, i-p));
	    p=i+1;
	}
    }
    ret.push_back(s.substr(p));
    return ret;
}


struct Dinic {
    typedef int Flow;
    static const Flow INF = 1<<29;
    struct Edge {
	int src, dst;
	Flow cap;
	int rev;
    };
    typedef vector<vector<Edge> > Graph;
    Graph G;
    vector<int>len, iter;
    Dinic(int N) : G(N) {}
    void add_edge(int u, int v, Flow c) {
	G[u].push_back((Edge){ u, v, c, (int)G[v].size() });
	G[v].push_back((Edge){ v, u, 0, (int)G[u].size()-1 });
    }
    Flow dfs(int v, int s, Flow c) {
	if (v == s || c == 0) return c;
	Flow ret = 0;
	for (int &i=iter[v]; i<(int)G[v].size(); i++) {
	    Edge &e = G[v][i], &re = G[e.dst][e.rev];
	    if (re.cap > 0 && len[v] > len[e.dst]) {
		Flow f = dfs(e.dst, s, min(c-ret, re.cap));
		ret += f;
		e.cap += f; re.cap -= f;
		if (ret == c) break;
	    }
	}
	return ret;
    }
    void bfs(int s) {
	len.assign(G.size(), -1);
	queue<int>qu;
	qu.push(s);
	len[s] = 0;
	for (;!qu.empty();) {
	    int v = qu.front(); qu.pop();
	    for (int i=0; i<(int)G[v].size(); i++) {
		const Edge &e = G[v][i];
		if (e.cap > 0 && len[e.dst] == -1) {
		    len[e.dst] = len[v] + 1;
		    qu.push(e.dst);
		}
	    }
	}
    }
    Flow _flow;
    Flow flow(int source, int sink) {
	Flow ret = 0;
	while (true) {
	    bfs(source);
	    if (len[sink] == -1) return _flow = ret;
	    iter.assign(G.size(), 0);
	    ret += dfs(sink, source, INF);
	}
    }
};
const Dinic::Flow Dinic::INF;


int N;
map<string, int> mp;
int cnt;
VI col;


vector<VI> D;
void line() {
    string buf;
    getline(cin, buf);
    vector<string> v = split(buf);
    VI w;
    EACH (e, v) {
	if (mp.count(*e) == 0) {
	    mp[*e] = cnt++;
	}
	w.push_back(mp[*e]);
    }
    D.push_back(w);
}

int main() {
    int T;
    // scanf("%d", &T);
    cin >> T;

    for (int tc=1; tc<=T; tc++) {
	// scanf("%d ", &N);
	string buf;
	cin >> N;

	getline(cin, buf);

	mp.clear();
	cnt = 0;
	col.clear();
	D.clear();
	
	REP (i, N) line();

	col.assign(cnt, 0);
	REP (i, 2) {
	    EACH (e, D[i]) {
		col[*e] |= (1<<i);
	    }
	}
	
	int BASE = cnt, SRC = BASE + cnt, SNK = SRC + 1;

	// eprintf("CNT %d\n", cnt);

	Dinic X(SNK+1);
	REP (i, cnt) {
	    X.add_edge(i, i+BASE, 1);
	    if (col[i] & 1) X.add_edge(SRC, i, X.INF);
	    if (col[i] & 2) X.add_edge(i+BASE, SNK, X.INF);
	}

	for (int i=2; i<N; i++) {
	    EACH (v, D[i]) EACH (w, D[i]) {
		X.add_edge(*v+BASE, *w, X.INF);
	    }
	}

	X.flow(SRC, SNK);
	cout << "Case #" << tc << ": " << X._flow << "\n";
	
	// printf("Case #%d: ", tc);
	
    }
    return 0;
}
