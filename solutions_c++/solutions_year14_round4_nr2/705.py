#include <cstdio>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

struct T {
	int val, id;
	T (int _val = 0, int _id = 0)
		: val(_val), id(_id) {}
};

bool operator< (T a, T b) {
	return a.val < b.val;
}

int a[10101];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int qwe;
	scanf("%d", &qwe);
	for (int t = 1; t <= qwe; t++) {
		printf("Case #%d: ", t);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		map<int, int> m;
		for (int i = 0; i < n; i++)
			m[a[i]] = i;
		set<int> s;
		for (int i = 0; i < n; i++)
			s.insert(a[i]);
		int l = 0, r = n - 1;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int val = *s.begin();
			s.erase(s.begin());
			int idx = m[val];
			if (r - idx > idx - l) {
				// move left
				for (int j = idx - 1; j >= l; j--) {
					m[a[j]] = j + 1;
					m[a[j + 1]] = j;
					swap(a[j], a[j + 1]);
					ans++;
				}
				l++;
			}
			else {
				// move right
				for (int j = idx; j < r; j++) {
					m[a[j]] = j + 1;
					m[a[j + 1]] = j;
					swap(a[j], a[j + 1]);
					ans++;
				}
				r--;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
