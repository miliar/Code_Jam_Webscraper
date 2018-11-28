#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

string a, b, tmpA, tmpB;

ll bestA, bestB, bestD = LLONG_MAX;
string ba, bb;
inline ll toLL(string &x) {
	ll res = 0;
	for (int i = 0; i < x.size(); ++i)
		res = 10 * res + (x[i] - '0');
	return res;
}

inline void equalize(int i) {
	if (a[i] == '?' && a[i] == b[i])
		a[i] = b[i] = '0';
	else if (a[i] == '?')
		a[i] = b[i];
	else if (b[i] == '?') b[i] = a[i];
}

inline void rpl(string &x, char r) {
	for (char &c : x)
		if (c == '?') c = r;
}
int n;

inline void bestize(string &a, string &b) {
	ll na = toLL(a), nb = toLL(b), diff = abs(na - nb);

	if (diff < bestD or diff == bestD && (na < bestA or na == bestA && nb < bestB))
	  bestD = diff, bestA = na, bestB = nb, ba = a, bb = b;
}

void bt(int ind) {
	if (ind == n) {
		bestize(a, b);
		return;
	}
	if (a[ind] == '?' && a[ind] == b[ind]) {
		a[ind] = b[ind] = '0';
		bt(ind + 1);
		a[ind] = b[ind] = '?';
		string newA = a, newB = b;
		newA[ind] = '1';
		newB[ind] = '0';
		rpl(newA, '0');
		rpl(newB, '9');
		bestize(newA, newB);

		newA = a, newB = b;
		newA[ind] = '0';
		newB[ind] = '1';
		rpl(newA, '9');
		rpl(newB, '0');
		bestize(newA, newB);

	}
	else if (a[ind] == '?') {
		a[ind] = b[ind];
		bt(ind + 1);
		a[ind] = '?';
		if (b[ind] != '9') {
			string newA = a, newB = b;
			newA[ind] = b[ind] + 1;
			rpl(newA, '0');
			rpl(newB, '9');
			bestize(newA, newB);
		}
		if (b[ind] != '0') {
			string newA = a, newB = b;
			newA[ind] = b[ind] - 1;
			rpl(newA, '9');
			rpl(newB, '0');
			bestize(newA, newB);
		}
	}
	else if (b[ind] == '?') {
		b[ind] = a[ind];
		bt(ind + 1);
		b[ind] = '?';
		if (a[ind] != '9') {
			string newA = a, newB = b;
			newB[ind] = a[ind] + 1;
			rpl(newA, '9');
			rpl(newB, '0');
			bestize(newA, newB);
		}
		if (a[ind] != '0') {
			string newA = a, newB = b;
			newB[ind] = a[ind] - 1;
			rpl(newA, '0');
			rpl(newB, '9');
			bestize(newA, newB);
		}
	}
	else {
		if (a[ind] < b[ind]) {
			string newA = a, newB = b;
			rpl(newA, '9');
			rpl(newB, '0');
			bestize(newA, newB);
		}
		else if (a[ind] > b[ind]) {
			string newA = a, newB = b;
			rpl(newA, '0');
			rpl(newB, '9');
			bestize(newA, newB);
		} else
			bt(ind + 1);
	}

}

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		cin >> a >> b;
		n = a.size();
		bestD = LLONG_MAX;
		bt(0);
		cout << "Case #" << cs << ": " << ba << ' ' << bb << '\n';
	}

	return 0;
}
