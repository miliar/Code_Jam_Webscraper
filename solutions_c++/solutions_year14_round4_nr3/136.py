#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll; typedef vector<pair<long long,long long> > vpll;
typedef vector<string> vs; typedef long double ld;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

inline bool commonPoint1D(int a, int b, int c, int d) {
	return c <= b && a <= d;
}

int calc(int a, int b, int c, int d, int y) {
	if(b < c) {
		return max(y, c - b - 1);
	}else if(d < a) {
		return max(y, a - d - 1);
	}else {
		return y;
	}
}

int X0[1000], Y0[1000], X1[1000], Y1[1000];
int g[1002][1002];
long long dist[1002];
bool vis[1002];


int main() {
	int T;
	scanf("%d", &T);
	rep(ii, T) {
		int W, H, B;
		scanf("%d%d%d", &W, &H, &B);
		rep(i, B)
			scanf("%d%d%d%d", &X0[i], &Y0[i], &X1[i], &Y1[i]);
		int s = B, t = B + 1;
		mset(g, INF);
		g[s][t] = W;
		rep(i, B) {
			g[s][i] = X0[i];
			g[i][t] = W - 1 - X1[i];
		}
		rep(i, B) rep(j, B) {
			int w = INF;
			if(Y1[i] < Y0[j]) amin(w, calc(X0[i], X1[i], X0[j], X1[j], Y0[j] - Y1[i] - 1));
			if(Y0[i] > Y1[j]) amin(w, calc(X0[i], X1[i], X0[j], X1[j], Y0[i] - Y1[j] - 1));
			if(X1[i] < X0[j]) amin(w, calc(Y0[i], Y1[i], Y0[j], Y1[j], X0[j] - X1[i] - 1));
			if(X0[i] > X1[j]) amin(w, calc(Y0[i], Y1[i], Y0[j], Y1[j], X0[i] - X1[j] - 1));
			g[i][j] = w;
		}
		rep(i, B) rep(j, B) if(g[i][j] != g[j][i])
			cerr << "Error! (assymetric)" << endl;
		mset(vis, 0);
		mset(dist, INF);
		dist[s] = 0;
		rep(iii, B + 2) {
			int v = -1;
			rep(i, B + 2) if(!vis[i])
				if(v == -1 || dist[v] > dist[i])
					v = i;
			if(v == -1) { cerr << "Error! (v==-1)" << endl; break; }
			vis[v] = true;
			rep(u, B + 2) if(g[v][u] < INF)
				amin(dist[u], dist[v] + g[v][u]);
		}
		long long ans = dist[t];
		printf("Case #%d: %lld\n", ii+1, ans);
	}
	return 0;
}
