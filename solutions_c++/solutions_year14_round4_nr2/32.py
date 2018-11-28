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
int A[2000];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d", &N);
		vector<PII> v;
		REP(i,0,N) {
			scanf("%d", A+i);
			v.push_back(PII(A[i], i));
		}
		sort(v.begin(), v.end());
		int res = 0;
		REP(i,0,N) {
			res += min(v[i].second, N-i-1-v[i].second);
			REP(j,i+1,N)
				if (v[j].second > v[i].second)
					v[j].second--;
		}
		printf("%d\n", res);
	}
	return 0;
}
