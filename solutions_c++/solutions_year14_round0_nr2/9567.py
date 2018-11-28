#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <stack>
#include <map>
#include <queue>
#include <set>
#include <cmath>

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
#define CPI (4.0*atan(1.0))
const int INF = 0x3f3f3f3f;
const double eps = 10e-9;
const double PI = 4.0*atan(1.0);

const int maxn = 10000 + 20;
int A[maxn];
int B[maxn];

int main() {
	int c, n;

	scanf("%d%d", &c, &n);
	for(int i=0; i<n; i++) scanf("%d", &A[i]);
	/*MSET(B, 0);
	int tmax = A[n-1];
	int tadd = 0;
	for(int i=n-2; i>=0; i--) {
		tmax = max(tmax, A[i]);
		if(A[i]<=c && tmax-A[i]>tadd) {
			tadd = tmax-A[i];
		}
		B[i] = tadd;
	}*/
	int ans = 0;
	int tmin = A[0];
	int j = 1;
	while(tmin > c) {
		tmin = A[j++];
	}
	for(int i=j; i<n; i++) {
		tmin = min(tmin, A[i]);
		//int tget = A[i] - tmin + B[i];
		int tget = A[i] - tmin;
		if(tget > 0) {
			int tlast = 0;
			int pp = i;
			int tpmin = A[pp++];
			while(tpmin > c+tget) tpmin = A[pp++];
			for(int k=pp; k<n; k++) {
				tpmin = min(tpmin, A[k]);
				tlast = max(tlast, A[k]-tpmin);
			}
			tget += tlast;
		}
		ans = max(ans, tget);
	}
	printf("%d\n", c+ans);

	return 0;
}
