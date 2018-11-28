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
#define ll long long
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
char str[1111];
int main() {
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++) {
		int S;
		scanf("%d", &S);
		scanf("%s", str);
		int ans = 0, cppl = 0;
		for(int extra = 0; extra <= 2000; extra++) {
			cppl = extra;
			bool ok = true;
			REP(j, S+1) {
				if(cppl < j && str[j] > '0') {
					ok = false;
					break;
				}
				cppl += str[j]-'0';
			}
			if(ok) {
				ans = extra;
				break;
			}
		}
		printf("Case #%d: %d\n", testc, ans);
	}
	return 0;
}
