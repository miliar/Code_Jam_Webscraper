#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

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
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

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
#define next NEXTHUI
#define prev PREVHUI
#define y1 Y1HUI

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

int n;
int a[2050], b[2050];
int res[2050];

bool check(int v) {
	forn(i, n)
		if (res[i] == -1) {
			if (i < v && a[i] >= a[v])
				return 0;
			if (i > v && b[i] >= b[v])
				return 0;
		}
	for (int i = v-1; i >= 0; i--)
		if (res[i] == -1 && b[i] == b[v] + 1)
			return 0;
		else if (res[i] == -1 && b[i] == b[v])
			break;
	
	for (int i = v+1; i < n; i++)
		if (res[i] == -1 && a[i] == a[v] + 1)
			return 0;
		else if (res[i] == -1 && a[i] == a[v])
			break;
	return 1;
}

int get() {
	ford(i, n)
		if (res[i] == -1 && check(i))
			return i;
	cerr << "rqrq" << endl;
	return -1;
}

void solve() {
	cin >> n;
	forn(i, n)
		cin >> a[i];
	forn(i, n)
		cin >> b[i];
	forn(i, n) 
		res[i] = -1;
	forn(i, n) {
		int v = get();
		res[v] = n - i;
	}
	forn(i, n)
		cout << " " << res[i];
	cout << endl;
}

int main ()
{
	int tt;
	cin >> tt;
	forn(ii, tt) {
		printf("Case #%d:", ii + 1);
		solve();
	}	
	return 0;
}
