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

int64 calc1(int64 n, int64 p) {
	if (n == 0) return 0;
	int64 now = 1ll << (n - 1);
	if (p <= now)
		return 0;
	int64 res = (calc1(n - 1, p - now) * 2 + 1);
	if (res + 1 < (1ll << n)) res ++;
	return res;
}

int64 calc2(int64 n, int64 p) {
	if (p >= (1ll << n)) return (1ll << n) - 1;
	int64 now = 1ll << (n - 1);
	if (p >= now)
		return (1ll << n) - 2;
	return (calc2(n - 1, p)) * 2;
}

void solve(){
	int64 n, p;
	cin >> n >> p;
	cout << calc1(n, p) << " " << calc2(n, p) << endl;
}

int main ()
{
//	freopen("input.txt", "r", stdin);
//   freopen("res", "w", stdout);

	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	//	puts("");
	}

	
	return 0;
}
