//venk13
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <cassert>
#include <numeric>

using namespace std;

#define sz(a) (int)(a.size())
#define len(a) (int)(a.length())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

map <int, int> cnt;
set <int> my;
int a[10000];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, cas = 1; cin >> t;
	while(t--) {
		cout << "Case #" << cas++ << ": ";
		cnt.clear(); my.clear();
		int n, x; cin >> n >> x;
		for(int i = 0; i < n; i++) {
			cin >> a[i];
			cnt[a[i]]++;
			my.insert(-a[i]);
		}
		sort(a, a + n);
		int count = 0;
		for(int i = n - 1; i >= 0; i--) {
			if(cnt[a[i]] == 0) continue;
			++count;
			cnt[a[i]]--;
			if(cnt[a[i]] == 0) {
				my.erase(-a[i]);
			}
			if(my.empty()) break;
			set <int>::iterator it = my.lower_bound(a[i] - x);
			if(it == my.end()) continue;
			int num = -(*it);
			cnt[num]--;
			if(cnt[num] == 0) {
				my.erase(-num);
			}
			if(my.empty()) break;
		}
		cout << count << '\n';
	}
	return 0;
}