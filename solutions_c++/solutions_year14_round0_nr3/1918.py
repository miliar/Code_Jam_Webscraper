#include <iostream>
#include <vector>
using namespace std;
int c, r, m;
vector<int> cnt;
bool f = false;
void generate(int i1, int ost) {
	if (ost < 0)
		return;
	if (f)
		return;
	if (i1 == 0) {
		for (int i = 0; i <= min(ost, c - 2); ++i) {
			if (f)
				return;
			cnt[i1] = i;
			generate(i1 + 1, ost - i);
		}
		return;
	}
	if (i1 == r) {
		if (ost == 0) {
			f = true;
			return;
		}
		else
			return;
	}
	if (i1 == 1) {
		if (f)
			return;
		cnt[i1] = cnt[0];
		generate(i1 + 1, ost - cnt[0]);
		return;
	}
	if (ost == 0) {
		return;
	}
	for (int i = cnt[i1 - 1]; i <= min(ost, c); ++i) {
		if (f)
			return;
		if (i == c - 1)
			continue;
		cnt[i1] = i;
		generate(i1 + 1, ost - i);
	}
	if (f)
		return;
	cnt[i1] = 0;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "case #" << t << ':' << '\n';
		cin >> r >> c >> m;
		if (m == c * r - 1) {
			cout << 'c';
			for (int i = 1; i < c; ++i)
				cout << '*';
			cout << '\n';
			for (int i = 1; i < r; ++i) {
				for (int j = 0; j < c; ++j)
					cout << '*';
				cout << '\n';
			}
			continue;
		}
		if (m == 0) {
			cout << 'c';
			for (int i = 0; i < c - 1; ++i)
				cout << '.';
			cout << '\n';
			for (int i = 1; i < r; ++i) {
				for (int j = 0; j < c; ++j)
					cout << '.';
				cout << '\n';
			}
			continue;
		}
		if (c == 1) {
			if (m > r - 2) {
				cout << "Impossible\n";
			}
			else {
				for (int i = 0; i < m; ++i)
					cout << '*' << '\n';
				for (int i = r - m - 1; i >= 1; --i)
					cout << '.' << '\n';
				cout << 'c';
				cout << '\n';
			}
			continue;
		}
		cnt.clear();
		cnt.resize(r);
		f = false;
		generate(0, m);
		if (!f) {
			cout << "Impossible\n";
			continue;
		}
		for (int j = 0; j < cnt[0]; ++j)
			cout << '*';
		for (int j = c - cnt[0] - 1; j >= 1; --j)
			cout << '.';
		cout << 'c';
		cout << '\n';
		for (int i = 1; i < r; ++i) {
			for (int j = 0; j < cnt[i]; ++j)
				cout << '*';
			for (int j = c - cnt[i]; j >= 1; --j)
				cout << '.';
			cout << '\n';
		}
	}
}