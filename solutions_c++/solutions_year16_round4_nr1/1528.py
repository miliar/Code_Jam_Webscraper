
#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;


bool correct(char a[], int idx) 
{
	while (idx > 1 && idx % 2 == 1) {
		if (a[idx] == a[idx - 1]) return false;
		if (a[idx] == 'P') {
			if (a[idx - 1] == 'R') {
				a[idx / 2] = 'P';
			}
			else {
				a[idx / 2] = 'S';
			}
		}
		else if (a[idx] == 'R') {
			if (a[idx - 1] == 'P') {
				a[idx / 2] = 'P';
			}
			else {
				a[idx / 2] = 'R';
			}
		}
		else {
			if (a[idx - 1] == 'P') {
				a[idx / 2] = 'S';
			}
			else {
				a[idx / 2] = 'R';
			}
		}
		idx /= 2;
	}
	return true;
}

bool solve(char a[], int idx, int n, int p, int r, int s)
{
	if (idx == n) {
		return true;
	}
	else {
		if (idx % 2 == 0) {
			if (p > 0) {
				a[n + idx] = 'P';
				if (correct(a, n + idx)) {
					if (solve(a, idx + 1, n, p - 1, r, s)) return true;
				}
			}
			if (r > 0) {
				a[n + idx] = 'R';
				if (correct(a, n + idx)) {
					if (solve(a, idx + 1, n, p, r - 1, s)) return true;
				}
			}
		}
		else {
			if (r > 0 && a[n + idx - 1] == 'P') {
				a[n + idx] = 'R';
				if (correct(a, n + idx)) {
					if (solve(a, idx + 1, n, p, r - 1, s)) return true;
				}
			}
			if (s > 0) {
				a[n + idx] = 'S';
				if (correct(a, n + idx)) {
					if (solve(a, idx + 1, n, p, r, s - 1)) return true;
				}
			}
		}
		
		
		return false;
	}
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int k, n, r, p, s;
	char buf[40];
	char a[1 << 13];
	 
	cin >> k;
	cin.getline(buf, 40);

	for (int t = 0; t < k; t++) {
		
		cin >> n >> r >> p >> s;

		int cnt = 1 << n;
		a[2 * cnt] = '\0';
		cout << "Case #" << t+1 << ": ";
		if (solve(a, 0, cnt, p, r, s)) {
			cout << string(a + cnt) << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}

	}

	cin.close();
	cout.close();

	return 0;
}
