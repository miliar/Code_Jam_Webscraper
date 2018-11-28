#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void fastInOut();

int getLstZero(string &n) {
	for (int i = int(n.size()) - 1; i >= 0; --i)
		if (n[i] == '-')
			return i;
	return -1;
}

int eval(string n) {
	int ret = 0, lstZero;
	while (1) {
		lstZero = getLstZero(n);
		if (lstZero == -1)
			break;
		if (n[0] == '+')
			++ret;
		for (int i = 0; i < int(n.size()) && n[i] == '+'; ++i)
			n[i] = '-';
		lstZero = getLstZero(n);
		if (lstZero == -1)
			break;
		++ret;
		for (int i = 0; i <= lstZero; ++i)
			n[i] = (n[i] == '+') ? '-' : '+';
		for (int i = 0; i < (lstZero + 1) / 2; ++i)
			swap(n[i], n[lstZero - i]);
	}
	return ret;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	fastInOut();
	int t;
	string n;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		cin >> n;
		cout << "Case #" << tst << ": " << eval(n) << "\n";
	}
	return 0;
}

void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
