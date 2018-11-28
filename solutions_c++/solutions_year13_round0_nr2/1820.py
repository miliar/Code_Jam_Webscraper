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

int n, m;
int a[200][200], b[200][200];

void solve(){
	cin >> n >> m;
	forn(i, n)
		forn(j, m) {
			cin >> a[i][j];
			b[i][j] = 100;
		}
	forn(i, n) {
		int now = 0;
		forn(j, m)
			now = max(now, a[i][j]);
		forn(j, m)
			b[i][j] = min(b[i][j], now);
	}
	forn(i, m) {
		int now = 0;
		forn(j, n)
			now = max(now, a[j][i]);
		forn(j, n)
			b[j][i] = min(b[j][i], now);
	}
	bool done = 1;
	forn(i, n)
		forn(j, m)
			if (b[i][j] != a[i][j])
				done = 0;
	if (done)
		puts("YES");
	else
		puts("NO");
}

int main ()
{
	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	}

	
	return 0;
}
