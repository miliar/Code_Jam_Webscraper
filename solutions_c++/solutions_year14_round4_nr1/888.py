#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
#define ll long long
#define inf 1000000000
#define L(s) ((int)(s).size())
#define x first 
#define y second
#define pii pair<int, int>
#define mp make_pair
int n, t, x;
multiset<int> a;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cin >> n >> x;
		a.clear();
		for(int i = 0; i < n; ++i) {
			int val;
			scanf("%d", &val);
			a.insert(val);
		}
		int ans = 0;
		while(L(a)) {
			++ans;
			multiset<int>::iterator i = a.end();
			--i;
			int val = *i;
			a.erase(i);
			if (!L(a)) break;
			multiset<int>::iterator j = a.upper_bound(x - val);
			if (j == a.begin()) continue;
			--j;
			a.erase(j);
		}
		cout << "Case #" << tc <<": ";
		cout << ans << endl;
	}
}
