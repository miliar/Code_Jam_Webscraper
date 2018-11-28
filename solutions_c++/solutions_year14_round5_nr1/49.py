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
ll f[2000000];
ll s[2000000];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		ll N, p, q, r, ss;
		scanf("%lld%lld%lld%lld%lld", &N, &p, &q, &r, &ss);
		s[0] = 0;
		REP(i,0,N) {
			f[i] = (i*p+q)%r+ss;
			s[i+1] = s[i]+f[i];
		}
		int a = 0;
		ll res = 2E18;
		REP(b,0,N) {
			while(a < b && max(s[a], s[b+1]-s[a]) > max(s[a+1], s[b+1]-s[a+1]))
				a++;
			res = min(res, max(max(s[a], s[b+1]-s[a]), s[N]-s[b+1]));
		}
		printf("%.10f\n", (double)(s[N]-res)/s[N]);
	}
	return 0;
}
