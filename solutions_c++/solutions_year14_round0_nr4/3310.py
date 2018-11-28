#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long double ld;

vector<ld> a, b, c, d;

int main() {
	int tt;
	cin >> tt;
	for (int o = 0; o < tt; o++) {
		a.clear();
		b.clear();
		int n;
		cin >> n;
		a.resize(n);
		b.resize(n);
		for (int i = 0; i < n; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
			cin >> b[i];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int ans1 = 0, ans2 = 0;
		c = a;
		d = b;
		for (int i = 0; i < n; i++) {
			int ind = lower_bound(b.begin(), b.end(), a[i]) - b.begin();
			if (ind == b.size())
				b.erase(b.begin()), ans2++;
			else
				b.erase(b.begin() + ind);
		}
		a = c;
		b = d;
		reverse(a.begin(), a.end());
		reverse(b.begin(), b.end());
		for (int i = 0; i < n; i++) {
			if (a[0] > b[0])
				ans1++, a.erase(a.begin());
			else
				a.pop_back();
			b.erase(b.begin());
		}
		cout << "Case #" << o + 1 << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}
