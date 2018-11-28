#include <stdio.h>
#include <stack>
#include <math.h>
#include <time.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <cassert>
#include <queue>
#include <fstream>

using namespace std;

typedef long long ll;
typedef long double ld;

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795


int main () {
#ifdef _DEBUG
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;	
	for (int j = 1; j <= t; j++) {
		int s_max;
		string s;
		cin >> s_max >> s;
		int cnt = 0, ans = 0;
		forn (i, s.size()) {
			if (cnt < i) {
				ans += i - cnt;
				cnt += i - cnt;
			} 
			cnt += s[i] - '0';
		}
		cout << "Case #" << j << ": " << ans << endl;
	}
	return 0;
}