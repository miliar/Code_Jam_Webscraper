//Orz Sevenkplus
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <complex>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#define un using namespace
un std;
#define pb push_back
#define pf pop_front

#define mp make_pair

#define c0 first
#define c1 second
#define sqr(x) ((x)*(x))
#define clr(x) memset(x, 0, sizeof(x))
#define clr1(x) memset(x, -1, sizeof(x))
#define clr80(x) memset(x, 0x80, sizeof(x))
#define clr7F(x) memset(x, 0x7F, sizeof(x))

#define LL long long
#ifdef __unix__
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif
#define pii pair<int, int>
#define pip pair<int, pii>
#define vi vector<int>
#define vpi vector<pii>
#define pq priority_queue

template<typename T>
inline bool chkmin(T &a, T b){return a > b ? a = b, 1 : 0;}
template<typename T>
inline bool chkmax(T &a, T b){return a < b ? a = b, 1 : 0;}

#define P 1000000007


#define getint(x){\
	char __next__char__;bool __nega__int__=0;\
	while(!isdigit(__next__char__=getchar())&&__next__char__!='-');\
	__next__char__=='-'?(x=0,__nega__int__=1):(x=__next__char__-48);\
	while(isdigit(__next__char__=getchar()))x=x*10+__next__char__-48;\
	if(__nega__int__)x=-x;\
}
#define getint2(x1,x2){getint(x1);getint(x2);}
#define getint3(x1,x2,x3){getint(x1);getint(x2);getint(x3);}
#define getint4(x1,x2,x3,x4){getint(x1);getint(x2);getint(x3);getint(x4);}
#define getint5(x1,x2,x3,x4,x5){getint(x1);getint(x2);getint(x3);getint(x4);getint(x5);}
#define getint6(x1,x2,x3,x4,x5,x6){getint(x1);getint(x2);getint(x3);getint(x4);getint(x5);getint(x6);}

char m[100][120];
int f[300][2];
int r, c;

bool check(int i, int j, int dx, int dy) {
	for (int x = i + dx, y = j + dy; 0 <= x && x < r && 0 <= y && y < c; x += dx, y += dy) {
		if (m[x][y] != '.')
			return true;
	}
	return false;
}

void solve() {
	getint2(r, c);
	for (int i = 0; i < r; i++) {
		scanf("%s", m[i]);
	}
	int ans = 0;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (m[i][j] != '.') {
				if (check(i, j, f[m[i][j]][0], f[m[i][j]][1]))
					goto end;
				if (check(i, j, 0, -1) ||
						check(i, j, 0, 1) ||
						check(i, j, -1, 0) ||
						check(i, j, 1, 0))
					ans++;
				else {
					puts("IMPOSSIBLE");
					return;
				}
			}
end:;
		}
	}
	printf("%d\n", ans);
}
int main() {
	f['<'][0] = f['>'][0] = f['^'][1] = f['v'][1] = 0;
	f['<'][1] = f['^'][0] = -1;
	f['>'][1] = f['v'][0] = 1;
	int T;
	getint(T);
	for(int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		solve();
	}
}
