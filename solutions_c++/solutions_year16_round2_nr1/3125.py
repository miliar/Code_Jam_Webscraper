#define DEBUG 0
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

char nums[] = { 'Z', 'W', 'U', 'X', 'G', 'O', 'R', 'F', 'V', 'N' };
int order[] = { 0, 2, 4, 6, 8, 1, 3, 5, 7, 9 };
string nnn[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int sizes[] = { 4, 3, 3, 5, 4, 4, 3, 5, 5, 4 };
map<char, int> m;
bool taken[2000];
bool found[5];
string s;
vector<int> phone;

bool find(int n)
{
	memset(found, 0, sizeof(found));
	vector<int> foundPos;
	for (int j = 0; j < s.size(); ++j) {
		if (!taken[j]) {
			for (int k = 0; k < sizes[n]; ++k) {
				if (!found[k] && s[j] == nnn[n][k]) {
					found[k] = true;
					foundPos.push_back(j);
					break;
				}
			}
		}
		if (foundPos.size() == sizes[n]) {
			break;
		}
	}
	if (foundPos.size() != sizes[n]) {
		return false;
	}
	for (int i = 0; i < foundPos.size(); ++i) {
		taken[foundPos[i]] = true;
	}
	return true;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cerr << fixed << setprecision(0);

	for (int i = 0; i < 10; ++i) {
		m[nums[i]] = i;
	}

	if (!DEBUG) {
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	}

	int _c, _start = static_cast<int>(clock());
	cin >> _c;

	for(int _cc = 1; _cc <= _c; ++_cc) {
		int _t = static_cast<int>(clock());
		cout << "Case #" << _cc << ": ";

		memset(taken, 0, sizeof(taken));
		cin >> s;

		vector<int> ans;
		for (int i = 0; i < 10; ++i) {
			while (find(order[i])) {
				ans.push_back(order[i]);
			}
		}

		sort(ans.begin(), ans.end());
		for (int i = 0; i < ans.size(); ++i) {
			cout << ans[i];
		}
		cout << endl;

		cerr << "[Case #" << _cc << " complete, " << static_cast<int>(clock() - _t) << " ms, " << 100. * _cc / _c << "%]" << endl;
	}

	cerr << "Total time: " << static_cast<int>(clock() - _start) << " ms" << endl;

	return 0;
}

