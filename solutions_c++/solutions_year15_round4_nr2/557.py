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

double r[100], c[100];
void solve() {
	int n;
	getint(n);
	double V, X;
	scanf("%lf%lf", &V, &X);
	for (int i = 0; i < n; i++)
		scanf("%lf%lf", r + i, c + i);
	if (n == 1) {
		if (c[0] == X)
			printf("%.10f\n", V / r[0]);
		else
			puts("IMPOSSIBLE");
	} else if (n == 2) {
		if (c[0] > X && c[1] > X)
			puts("IMPOSSIBLE");
		else if (c[0] < X && c[1] < X)
			puts("IMPOSSIBLE");
		else if (c[0] == X && c[1] == X)
			printf("%.10f\n", V / (r[0] + r[1]));
		else {
			double v2 = V * (X - c[0]) / (c[1] - c[0]);
			double v1 = V - v2;
			printf("%.10f\n", max(v1 / r[0], v2 / r[1]));
		}
	}
}
int main() {
	int T;
	getint(T);
	for(int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		solve();
	}
}
