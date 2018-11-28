
#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

double yes[16], t_yes[16];

double solve(double a[], bool used[], int idx, int k_idx, int n, int k)
{
	if (k_idx > 2 * k) return 0.0;
	if (idx == n) {

		if (k_idx != 2 * k) return 0.0;
		for (int i = 0; i < n; i++) {
			yes[i] = 0.0;
		}
		yes[0] = 1.0;

		for (int j = 0; j < n; j++) {
			if (used[j]) {
				for (int i = 0; i < n; i++) {
					t_yes[i] = yes[i];
				}
				for (int i = 0; i < n; i++) {
					yes[i] = t_yes[i] * (1 - a[j]) + t_yes[i - 1] * a[j];
				}
			}
		}
		return yes[k];
	}
	else {

		double t, res = 0.0; 
		
		used[idx] = false;
		t = solve(a, used, idx + 1, k_idx, n, k);
		if (t > res) res = t;
		
		used[idx] = true;
		t = solve(a, used, idx + 1, k_idx + 1, n, k);
		if (t > res) res = t;

		return res;
	}
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int k, n, m;
	char buf[40];
	double a[16];
	bool used[16];
	 
	cin >> k;
	cin.getline(buf, 40);

	for (int t = 0; t < k; t++) {
		
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			used[i] = false;
		}
		cout << "Case #" << t+1 << ": ";
		cout << solve(a, used, 0, 0, n, m / 2) << endl;
	}

	cin.close();
	cout.close();

	return 0;
}
