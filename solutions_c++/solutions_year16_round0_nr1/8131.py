#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

int a[10];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	ifstream fin("input.in");
	ofstream fout("output.out");
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
	int t, test;
	long long n;
	fin >> t;
	for (int j = 1; j <= t; j++) {
		fout << "Case #" << j << ": ";
		fin >> n;
		if (n == 0) {
			fout << "INSOMNIA" << endl;
			continue;
		}
		for (int i = 0; i < 10; i++) {
			a[i] = 0;
		}
		for (int i = 1; i <= 72; i++) {
			test = i * n;
			while (test > 0) {
				a[test % 10]++;
				test /= 10;
			}
			int c = 0;
			for (int j = 0; j < 10; j++) {
				if (a[j] > 0) {
					c++;
				}
			}
			if (c == 10) {
				fout << (n * i) << endl;
				break;
			}
		}
	}
}