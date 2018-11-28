#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define inf 1000000000
#define N 1024

int x1[N], x2[N], y2[N];
int yy[N];
int n, m, b;
vector <int> E[N], W[N];


int D (int a1, int a2, int b1, int b2){
	if (a1 > b1){
		swap(a1,b1), swap(a2, b2);
	}
	
	return max (0, b1-a2-1);
}


struct no{
	int v, dist;
	bool operator < (const no &e) const {
		return dist > e.dist;
	}
};

int dist[N];

int dijkstra (){
	priority_queue <no> Q;
	f (i, 0, b+2) dist[i] = inf;
	dist[b] = 0;
	no e; e.v = b, e.dist = 0;
	Q.push(e);
	while (!Q.empty()){
		e = Q.top(); Q.pop();
		int v = e.v;
		if (v == b+1) return dist[v];
		if (e.dist != dist[v]) continue;
		f (i, 0, E[v].size()){
			int viz = E[v][i], p = W[v][i];
			if (dist[viz] > p+dist[v]){
				dist[viz] = p+dist[v];
				e.v = viz, e.dist = dist[viz];
				Q.push(e);
			}
		}
	}
	return -1;
}


int main (){
	int t; cin >> t;
	f (tt, 1, t+1){
		cin >> n >> m >> b;
		f (i, 0, b){
			cin >> x1[i] >> yy[i] >> x2[i] >> y2[i];
		}
		f (i, 0, b+2) E[i].clear(), W[i].clear();

		f (i, 0, b){
			E[b].pb(i); E[i].pb(b);
			W[b].pb(x1[i]); W[i].pb(x1[i]);
			E[b+1].pb(i); E[i].pb(b+1);
			W[b+1].pb(n-x2[i]-1); W[i].pb(n-x2[i]-1);
		}
		E[b].pb(b+1), E[b+1].pb(b);
		W[b].pb(n), W[b+1].pb(n);

		f (i, 0, b) f (j, i+1, b){
			int d = max (D(x1[i], x2[i], x1[j], x2[j]), D(yy[i], y2[i], yy[j], y2[j]));
			E[i].pb(j), W[i].pb(d);
			E[j].pb(i), W[j].pb(d);
		}

		printf("Case #%d: %d\n", tt,dijkstra());

	}
	return 0;
}
