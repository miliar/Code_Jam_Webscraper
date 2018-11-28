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
#define MOD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,n) for (int i = 0; i < (n); i++)

int T, N;
char zeile[1000];
long double prob[1<<20];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%s ", zeile);
		N = strlen(zeile);
// 		fprintf(stderr, "N = %d\n", N);
		int startnr = 0, startfilled = 0;
		REP(i, N)
			if (zeile[i] == 'X') {
				startnr |= 1<<i;
				startfilled++;
			}
// 		printf("startnr = %d\n", startnr);
		REP(i, 1<<N)
			prob[i] = 0;
		long double res = 0;
		prob[startnr] = 1;
		for (int f = startfilled; f < N; f++) {
			REP(nr, 1<<N) {
				int anz = 0;
				REP(i, N)
					anz += (nr>>i)&1;
				if (anz != f)
					continue;
// 				fprintf(stderr, "prob[%d] = %lf\n", nr, prob[nr]);
				REP(i, N) {
					int a = 0;
					while(nr&(1<<((i+a)%N)))
						a++;
					res += prob[nr]*(N-a)/N;
					prob[nr|(1<<((i+a)%N))] += prob[nr]/N;
				}
			}
		}
		printf("%.15Lf\n", res);
	}
	return 0;
}
