#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <queue>
#include <set>

using namespace std;

//#define WIN
#ifdef WIN
typedef __int64 LL;
#define iform "%I64d"
#define oform "%I64d\n"
#else
typedef long long LL;
#define iform "%lld"
#define oform "%lld\n"
#endif

#define SI(a) scanf("%d", &(a))
#define SDI(a, b) scanf("%d%d", &(a), &(b))
#define S64I(a) scanf(iform, &(a))
#define SS(a) scanf("%s", (a))
#define SDS(a, b) scanf("%s%s", (a), (b))
#define SC(a) scanf("%c", &(a))
#define PI(a) printf("%d\n", (a))
#define PS(a) puts(a)
#define P64I(a) printf(oform, (a))
#define Max(a, b) ((a) > (b) ? (a) : (b))
#define Min(a, b) ((a) < (b) ? (a) : (b))
#define MSET(a, b) (memset((a), (b), sizeof(a)))
#define Mid(L, R) ((L) + ((R) - (L))/2)
#define Abs(a) ((a) >= 0 ? (a) : -(a))
#define REP(i, n) for(int (i)=0; (i) < (n); (i)++)
#define FOR(i, a, n) for(int (i)=(a); (i) <= (n); (i)++)
const int INF = 0x3f3f3f3f;
const double eps = 10e-9;

const int maxn = 5;
int A[maxn][maxn];
int B[maxn][maxn];
int f[maxn];
int s[maxn];

int main() {
	int T;

	//freopen("./gcj_a.in", "r", stdin);
	//freopen("./gcj_a.out", "w", stdout);
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		int a, b;
		scanf("%d", &a);
		for(int i=1; i<=4; i++) {
			for(int j=1; j<=4; j++) {
				scanf("%d", &A[i][j]);
				if(i==a) f[j] = A[i][j];
			}
		}
		scanf("%d", &b);
		for(int i=1; i<=4; i++) {
			for(int j=1; j<=4; j++) {
				scanf("%d", &B[i][j]);
				if(i==b) s[j] = B[i][j];
			}
		}
		int same = 0;
		int ans = 0;
		for(int i=1; i<=4; i++) {
			for(int j=1; j<=4; j++) if(f[i]==s[j]) {
				same++;
				ans = f[i];
			}
		}
		printf("Case #%d: ", kase);	
		if(same==0) {
			puts("Volunteer cheated!");
		} else if(same==1) {
			printf("%d\n", ans);
		} else {
			puts("Bad magician!");
		}
		
	}

	return 0;
}
