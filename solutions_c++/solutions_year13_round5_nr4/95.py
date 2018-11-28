#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

double dp[2000000];
double ways[2000000];

int nowCase = 0;

void solve() {
	string s;
	cin >> s;
	int n = s.size();
	REP(i, (1 << n)) dp[i] = ways[i] = 0.0;
	int initMask = 0;
	REP(i, n) {
		if (s[i] == 'X') {
			initMask |= 1 << i;
		}
	}

	dp[initMask] = 0.0;
	ways[initMask] = 1.0;
	for (int i = 0; i < (1 << n); ++i) {
		if ((i & initMask) != initMask) continue;
		if (i + 1 == (1 << n)) break;
		for (int j = 0; j < n; ++j) {
			int dis = 0, next;
			for (int k = 0; k < n; ++k) {
				if ((i & (1 << ((j + k) % n)))) {
					++dis;
				} else {
					next = (j + k) % n;
					break;
				}
			}
			//if(i==2) cout << "j = " << j << " next = " << next << endl;
			dp[i | (1 << next)] += (dp[i] + (n - dis) * ways[i]);
			ways[i | (1 << next)] += ways[i];
		}
	}
	double ans = dp[(1 << n) - 1] / ways[(1 << n) - 1];
	printf("Case #%d: %.10f\n", ++nowCase, ans);
}

int main() {
	int T;
	cin >> T;
	while (T--) {
		solve();
	}

	return 0;
}