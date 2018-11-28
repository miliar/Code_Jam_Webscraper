#define _USE_MATH_DEFINES
 
#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>
 
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
 
using namespace std;
 
typedef long long li;
typedef long double ld;
 
typedef pair<int,int> point;
#define X first
#define Y second
 
int n;
double w1[1005], w2[1005];
 
int main() {
#ifdef dans
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
 
	int t;
	cin >> t;
	forn(tt, t) {
		cin >> n;
		forn(i, n)
			cin >> w1[i];
		sort(w1, w1+n);
		forn(i, n)
			cin >> w2[i];
		sort(w2, w2+n);
		int ptr = 0, a = 0, b = 0;
		forn(i, n) {
			if (w1[i] > w2[ptr])
				ptr++, a++;
		}
		int r = n-1;
		forn(i, n)
			if (w1[n-i-1] > w2[r]) {
				b++;
			} else
				r--;
		cout << "Case #" << tt+1 << ": " << a << " " << b << endl;
	}
 
	return 0;
}
