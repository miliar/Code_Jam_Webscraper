#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <assert.h>
#include <math.h>
#include <string.h>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,a,n) for (int i = (a); i < (n); i++)

int T;
int N;
long double V, X;
long double R[200];
long double C[200];
vector<int> sl;

bool cmp(int a, int b) {
	return C[a] < C[b];
}

bool isok(long double B) {
	long double minvx = 0, maxvx = 0;
	long double remv = V;
	REP(ii,0,N) {
		int i = sl[ii];
		long double h = min(remv, B*R[i]);
		minvx += C[i]*h;
		remv -= h;
	}
	remv = V;
	REP(ii,0,N) {
		int i = sl[N-ii-1];
		long double h = min(remv, B*R[i]);
		maxvx += C[i]*h;
		remv -= h;
	}
	return minvx <= V*X && V*X <= maxvx;
}

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d%Lf%Lf", &N, &V, &X);
		sl.clear();
		REP(i,0,N) {
			scanf("%Lf%Lf", R+i, C+i);
			sl.push_back(i);
		}
		sort(sl.begin(), sl.end(), cmp);
		long double a = 0, b = 1e10;
		if (!isok(b))
			printf("IMPOSSIBLE\n");
		else {
			while(abs(b-a) > 1e-10) {
				long double m = (a+b)/2;
				if (isok(m))
					b = m;
				else
					a = m;
			}
			printf("%.9Lf\n", a);
		}
	}
	return 0;
}
