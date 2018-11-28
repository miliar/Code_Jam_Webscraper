#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

double dp[22][1 << 22];
string s;
int n;

void pre_calc() {
	memset(dp, 0, sizeof dp);
	forn(k, 21) {
		forn(i, 1 << k) {
			dp[k][i] = k * k;
			if (i == 0) {
				dp[k][i] = 0;
				continue;
			}
			forn(j, k) {
				int now = i;
				int w = j;
				while(1) {
					if (w == k) w = 0;
					if (now & (1 << w)) {
						dp[k][i] += dp[k][i ^ (1 << w)];
						break;
					}
					dp[k][i] --;
					w ++;
				}
			}
			dp[k][i] /= k;
		}
	}

}

void solve(){
	cin >> s;
	int st = 0;
	n = s.size();
	ford(i, s.size()) {
		st = st * 2;
		if (s[i] == '.')
			st ++;
	}
	printf("%0.9lf\n", dp[n][st]);
}

int main ()
{
//	freopen("input.txt", "r", stdin);
//   freopen("res", "w", stdout);

	pre_calc();
	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	}

	
	return 0;
}
