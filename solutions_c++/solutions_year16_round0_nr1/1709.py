#include <bits/stdc++.h>
typedef long long LL;
using namespace std;
#define ALL(x) (x.begin(), x.end())
#define rep(i,n) for(int i = 0;i < n;i ++)

void insert(int x, set<int> &s) {
	while(x) {
		s.insert(x % 10);
		x /= 10;
	}
}

int main() {
	//freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int T, n;
	cin >> T;
	rep(cas, T) {
		cin >> n;
		cout << "Case #" << cas + 1 << ": ";
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		set<int> sets;
		insert(n, sets);
		int m = n;
		while(sets.size() < 10) {
			m += n;
			insert(m, sets);
		}
		cout << m << endl;
	}
	return 0;
}

