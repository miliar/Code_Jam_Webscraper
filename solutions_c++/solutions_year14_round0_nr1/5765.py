#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define FOR(i,a,b) for(__typeof(b) i=(a);i!=(b);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define EACH(i,a) FOR(i,a.begin(),a.end())
#define PB push_back
#define iss istringstream
#define SZ(a) (int)a.size()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long

int T, A, B;

int mem[5][5];
int mem2[5][5];
int dp[25];

int main() {
	scanf("%d", &T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%d", &A);
		CLEAR(dp);
		for(int i = 1 ; i <= 4 ; i++) {
			for(int j = 1 ; j <= 4 ; j++) {
				scanf("%d", &mem[i][j]);
			}
		}
		scanf("%d", &B);
		for(int i = 1 ; i <= 4 ; i++) {
			for(int j = 1 ; j <= 4 ; j++) {
				scanf("%d", &mem2[i][j]);
			}
		}
		for(int j = 1 ; j <= 4 ; j++) {
			dp[mem[A][j]]++;
			dp[mem2[B][j]]++;
		}
		vector<int> v;
		for(int i = 1 ; i <= 16 ; i++) {
			if (dp[i] == 2) {
				v.push_back(i);
			}
		}
		if (SZ(v) >= 2) {
			printf("Case #%d: Bad magician!\n", t);
		}	else if (SZ(v) == 0) {
			printf("Case #%d: Volunteer cheated!\n", t);
		}	else {
			printf("Case #%d: %d\n", t, v[0]);
		}
	}
	return 0;
}
