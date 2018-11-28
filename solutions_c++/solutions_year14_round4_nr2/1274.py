#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define REP(i, N) for(int i = 0; i < (N); i++)
int A[20];
int n;
using namespace std;
int main() {
	int T, testcase=1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &n);
		REP(i, n) scanf("%d", A+i);
		int ans = 1000000000;
		REP(i, 1<<n) {
			vector<int> first, second;			
			REP(j, n) if(i&(1<<j)) first.pb(A[j]); else second.pb(A[j]);
			int cans = 0;
			REP(j, n) {
				if(i&(1<<j)) for(int k = 0; k < j; k++) if(!(i&(1<<k))) cans++;
			}
			REP(j, first.size()) for(int k = j+1; k < first.size(); k++) if(first[j] > first[k]) cans++;
			REP(j, second.size()) for(int k = j+1; k < second.size(); k++) if(second[j] < second[k]) cans++;

			ans = min(cans, ans);
		}

		printf("Case #%d: ", testcase++);
		printf("%d\n", ans);
	}
	
	return 0;
}
