#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#ifndef ONLINE_JUDGE
	#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#else
	#define DEBUG(x) do {} while(0);
#endif

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
typedef long long ll;
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
int N,J,T;
void solve() {
	scanf("%d%d", &N, &J);
	int cnt = 0;
	int proof[11];
	for(ll i = (1LL<<(N-1))+1; cnt < J; i+=2) {
		bool ok = true;
		for(int b = 2; b <= 10; b++) {
			ll val = 0;
			REP(j, N) if((i&(1LL<<j))==0) {
				val = b*val + 0;
			} else {
				val = b*val + 1;
			}
			//printf("in base %d: %lld\n", b, val);
			bool found = false;
			for(int i = 2; i <= 1000; i++)
				if(val % i == 0) {
					proof[b] = i;
					found = true;
					break;
				}
			if(!found) {
				ok = false;
				break;
			}
		}
		if(ok) {
			REP(j, N) printf("%d", (i&(1LL<<j))==0?0:1);
			for(int b = 2; b <= 10; b++)
				printf(" %d", proof[b]);
			printf("\n");
			cnt++;
		}
	}
}

int main() {
	scanf("%d", &T);
	REP(testc, T) {
		printf("Case #%d:\n", testc+1);
		solve();
	}
	return 0;
}
