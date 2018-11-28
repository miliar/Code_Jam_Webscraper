#include <bits/stdc++.h>
using namespace std;

long long mindif;
string mina, minb;

void rec(string a, string b, int pos, long long va, long long vb, int dec) {
	if (pos < a.length()) {
		if (dec == 0) {
			if (a[pos] == '?' && b[pos] != '?') {
				a[pos] = '9';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}
			else if (a[pos] != '?' && b[pos] == '?') {
				b[pos] = '0';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}
			else if (a[pos] == '?' && b[pos] == '?') {
				a[pos] = '9';
				b[pos] = '0';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}
			else {
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}
		}
		else if (dec == 1) {
			if (a[pos] == '?' && b[pos] != '?') {
				if (b[pos] != '0') {
					a[pos] = b[pos] - 1;
					rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 0);
				}
				a[pos] = b[pos];
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 1);
				if (b[pos] != '9') {
					a[pos] = b[pos] + 1;
					rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 2);
				}
			}
			else if (a[pos] != '?' && b[pos] == '?') {
				if (a[pos] != '0') {
					b[pos] = a[pos] - 1;
					rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 2);
				}
				b[pos] = a[pos];
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 1);
				if (a[pos] != '9') {
					b[pos] = a[pos] + 1;
					rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 0);
				}
			}
			else if (a[pos] == '?' && b[pos] == '?') {
				a[pos] = '0';
				b[pos] = '1';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 0);
				a[pos] = b[pos] = '0';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 1);
				a[pos] = '1';
				b[pos] = '0';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 2);
			}
			else {
				if (a[pos] < b[pos])
					rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 0);
				else if (a[pos] == b[pos])
					rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 1);
				else
					rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', 2);
			}
		}
		else if (dec == 2) {
			if (a[pos] == '?' && b[pos] != '?') {
				a[pos] = '0';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}
			else if (a[pos] != '?' && b[pos] == '?') {
				b[pos] = '9';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}
			else if (a[pos] == '?' && b[pos] == '?') {
				a[pos] = '0';
				b[pos] = '9';
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}
			else {
				rec(a, b, pos + 1, va * 10 + a[pos] - '0', vb * 10 + b[pos] - '0', dec);
			}

		}
	}
	else if (abs(va - vb) < mindif || abs(va - vb) == mindif && make_pair(mina, minb) > make_pair(a, b)) {
		mindif = abs(va - vb);
		mina = a;
		minb = b;
	}
}

void solve(){
	string a, b;
	cin >> a >> b;

	mindif = 2e18;

	rec(a, b, 0, 0, 0, 1);

	cout << mina << " " << minb;
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
