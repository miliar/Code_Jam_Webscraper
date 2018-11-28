#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wunused-result"
#else
#define _CRT_SECURE_NO_WARNINGS
#define _SCL_SECURE_NO_WARNINGS
#endif
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <string>
#include <iostream>
#include <tuple>
#define FOR(x,y,z) for (int x=(y); x<=(z); ++x)
#define FORD(x,y,z) for(int x=(y); x>=(z); --x)
#define REP(x,y) for (int x=0; x<(y); ++x)
#if defined(__GNUC__) && __cplusplus < 201103L
#define FOREACH(y,x) for (typeof((x).begin()) y = (x).begin(); y != (x).end(); ++y)
#else
#define FOREACH(y,x) for (auto y = (x).begin(); y != (x).end(); ++y)
#endif
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef tuple<int,int,int> T3;
const int INF = 1000000001;

inline int Pow2(int exp) { return 1 << exp; }

template<typename T>
inline T Pow2(int exp) { return (T)1 << exp; }

int xp[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int yp[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };

bool AnyNbMines(int r, int c, int b, int x, int y)
{
	REP(i,8) {
		int xx = x + xp[i];
		int yy = y + yp[i];
		if (xx >= 0 && xx < r && yy >= 0 && yy < c && (b & Pow2(xx*c+yy))) return true;
	}
	return false;
}

int Bfs(int r, int c, int b, int x0, int y0)
{
	if (AnyNbMines(r,c,b,x0,y0)) return 1;
	queue<PII> q;
	q.push(PII(x0,y0));
	int res = 1, vs = Pow2(x0*c+y0);
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		REP(i,8) {
			int xx = x + xp[i];
			int yy = y + yp[i];
			int pp = Pow2(xx*c+yy);
			if (xx >= 0 && xx < r && yy >= 0 && yy < c && !(b&pp) && !(vs&pp)) {
				vs |= pp;
				++res;
				if (!AnyNbMines(r,c,b,xx,yy)) q.push(PII(xx,yy));
			}
		}
	}
	return res;
}

void CheckAll(int r, int c, map<T3,T3>& res)
{
	REP(k,Pow2(r*c)) {
		int m = 0;
		REP(i,r*c) m += (k >> i) & 1;
		if (res.count(T3(r,c,m)) == 1) continue;
		REP(i,r) {
			REP(j,c) {
				if (k & Pow2(i*c+j)) continue;
				if (Bfs(r, c, k, i, j) == r*c-m) res[T3(r,c,m)] = T3(k,i,j);
			}
		}
	}
}

int main(int argc, char** argv)
{
	map<T3,T3> res;
	FOR(i,1,5) {
		FOR(j,1,5) CheckAll(i,j,res);
	}
	int tc;
	scanf("%d", &tc);
	FOR(tccc,1,tc) {
		int r,c,m;
		scanf("%d%d%d", &r, &c, &m);
		printf("Case #%d:\n", tccc);
		auto it = res.find(T3(r,c,m));
		if (it == res.end()) printf("Impossible\n");
		else {
			T3 t = it->second;
			REP(i,r) {
				REP(j,c) {
					if (i == get<1>(t) && j == get<2>(t)) printf("c");
					else if (get<0>(t) & Pow2(i*c+j)) printf("*");
					else printf(".");
				}
				printf("\n");
			}
		}
	}

#ifdef _DEBUG
	system("pause");
#endif
	return 0;
}
