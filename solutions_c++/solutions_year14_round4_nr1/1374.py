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

using namespace std;
int usable[11111];
int prev[777];
int main() {
	int T, testcase=1;
	scanf("%d", &T);
	while(T--) {
		int n, X;
		scanf("%d%d", &n, &X);
		multiset<int> S;
		REP(i, n) { int s; scanf("%d", &s);S.insert(s);}
		int ans = 0;
		while(S.size() > 0) {
			multiset<int>::reverse_iterator Q = S.rbegin();
			int val = *Q;
			S.erase(S.find(val));
			int rem = X-val;
			multiset<int>::iterator QQ = S.upper_bound(rem);
			if(QQ != S.begin()) {
				QQ--;
				S.erase(QQ);
			}
			ans++;
		}

		printf("Case #%d: %d", testcase++, ans);
		printf("\n");
	}
	
	return 0;
}
