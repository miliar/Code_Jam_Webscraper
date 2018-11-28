#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void fastInOut();

const int mul[] = { 2, 3, 5, 7 };
int pws[11][32][4];

void init() {
	for (int i = 2; i <= 10; ++i) {
		int cur[] = { 1, 1, 1, 1 };
		for (int j = 0; j < 32; ++j)
			for (int k = 0; k < 4; ++k)
				pws[i][j][k] = cur[k], cur[k] = (cur[k] * i) % mul[k];
	}
}

bool addTwo(string &num) {
	int i;
	for (i = int(num.size()) - 2; i >= 0 && num[i] == '1'; --i)
		num[i] = '0';
	if (i == -1)
		return 0;
	num[i] = '1';
	return 1;
}

vector<int> calc(int n, string num) {
	vector<int> ret;
	for (int i = 2; i <= 10; ++i) {
		int cur[] = { 0, 0, 0, 0 };
		for (int j = n - 1; j >= 0; --j) {
			if (num[j] == '0')
				continue;
			for (int k = 0; k < 4; ++k)
				cur[k] = (cur[k] + pws[i][n - j - 1][k]) % mul[k];
		}
		for (int j = 0; j < 4; ++j)
			if (cur[j] == 0) {
				ret.push_back(mul[j]);
				goto nxt;
			}
		return vector<int>();
		nxt: ;
	}
	return ret;
}

vector<pair<string, vector<int> > > eval(int n, int j) {
	string num = "";
	for (int i = 0; i < n; ++i)
		num += (i == 0 || i == n - 1) ? "1" : "0";
	vector<pair<string, vector<int> > > ret;
	do {
		vector<int> cur = calc(n, num);
		if (!cur.empty())
			ret.push_back(make_pair(num, cur));
	} while (int(ret.size()) < j && addTwo(num));
	return ret;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	fastInOut();
	int t, n, j;
	cin >> t, init();
	for (int tst = 1; tst <= t; ++tst) {
		cin >> n >> j;
		vector<pair<string, vector<int> > > ret = eval(n, j);
		cout << "Case #" << tst << ":\n";
		for (int i = 0; i < int(ret.size()); ++i) {
			cout << ret[i].first;
			for (int k = 0; k < int(ret[i].second.size()); ++k)
				cout << " " << ret[i].second[k];
			cout << "\n";
		}
	}
	return 0;
}

void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
