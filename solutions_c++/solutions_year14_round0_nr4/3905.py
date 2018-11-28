#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
#define rep(i, a) for(int i = 0; i < (a); i++)
#define foru(i, s, e) for(int i = (s); i < (e); i++)
#define ford(i, s, e) for(int i = (s); i >= (e); i--)
#define cinNewLine cin.ignore(numeric_limits<streamsize>::max(), '\n');
const double EPS = 1e-9;
const int INF = 2147483647;
const LL LLINF = 9223372036854775807LL;
template <class T> T gcd(T a, T b) { if(a < b) swap(a, b); if(b == 0) return a; return gcd(b, a%b); }
template <class T> T lcm(T a, T b) { return (a*b)/gcd(a, b); }

int main() {
	int T;
	cin >> T;
	foru(t, 1, T+1) {
		int n;
		cin >> n;
		vector<double> naomi(n), ken(n);
		rep(i, n) {
			cin >> naomi[i];
		}
		rep(i, n) {
			cin >> ken[i];
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int i = 0, j = 0, ans1 = 0, ans2 = n;
		while(i < n) {
			if(naomi[i] > ken[j]) {
				ans1++;
				j++;
			}
			i++;
		}
		i = 0, j = 0;
		while(j < n) {
			if(ken[j] > naomi[i]) {
				ans2--;
				i++;
			}
			j++;
		}
		printf("Case #%d: %d %d\n", t, ans1, ans2);
	}
	return 0;
}

