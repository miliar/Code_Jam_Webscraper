#include <iostream>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <string>
#include <string.h>
using namespace std;
#define PI 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#define oo (1e9)+1
#define MOD 1000000007
#define all(x) x.begin(),x.end()
#define srta(x) sort(all(x))
#define rall(x) x.rbegin(),x.rend()
#define srtd(x) sort(rall(x))
#define set(a,b) memset(a,b,sizeof(a))
#define pb(a) push_back(a)
#define pbb() pop_back()
#define mp(a,b) make_pair(a,b)
#define sf(a) scanf("%d",&a)
#define pf(a) printf("%d\n",a)
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef double dd;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<vector<pii> > vvpii;
typedef set<int> si;
typedef map<int, int> mii;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		int n;
		cin >> n;
		cout << "Case #" << tc << ": ";
		if (!n) {
			cout << "INSOMNIA\n";
			continue;
		}
		set<int> s;
		ll res = 0;
		while (s.size() != 10) {
			res++;
			ll tmp = n*res;
			while (tmp) {
				s.insert(tmp % 10);
				tmp /= 10;
			}
		}
		cout << res*n << endl;
	}
	return 0;
}