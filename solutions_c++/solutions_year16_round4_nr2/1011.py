#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>

using namespace std;

bool check(vector <int> a) {
	vector <int> temp;
	while (!(a.size() == 1)) {
		temp.clear();
		for (int i = 0; i < a.size(); i += 2) { 
			if (a[i] == a[i+1])
				return false;
			int mn = min(a[i], a[i+1]);
			int mx = max(a[i], a[i+1]);
			if (mn == 1 && mx == 2)
				temp.push_back(1);
			else if (mn == 2 && mx == 3)
				temp.push_back(2);
			else
				temp.push_back(3);
		}
		a = temp;
	}
	return true;
}

int count_ones(int a) {
	int count = 0;
	while (a) {
		++count;
		a &= (a-1);
	}
	return count;
}

int main () {
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		/*int n, r, p, s;
		cin >> n >> r >> p >> s;
		vector <int> a;
		for (int j = 0; j < p; ++j)
			a.push_back(1);
		for (int j = 0; j < r; ++j)
			a.push_back(2);
		for (int j = 0; j < s; ++j)
			a.push_back(3);
		int fact = 1;
		for (int j = 1; j <= (1<<n); ++j)
			fact *= j;
		int count = 0;
		while (!check(a) && count < fact) {
			next_permutation(a.begin(), a.end());
			++count;
		}
		if (check(a))
			for (int j = 0; j < a.size(); ++j)
				if (a[j] == 1)
					cout << "P";
				else if (a[j] == 2)
					cout << "R";
				else
					cout << "S";
		else
			cout << "IMPOSSIBLE";
		cout << endl;*/

		int k, n;
		cin >> n >> k;
		long double mx = 0.;
		vector <long double> p (n);
		for (int j = 0; j < n; ++j)
			cin >> p[j];

		for (int j = 0; j < (1 << n); ++j) {
			int cur = j;
			if (count_ones(cur) != k)
				continue;

			vector <int> cand;
			cand.reserve(k);
			for (int d = 0; d < n; ++d) {
				if (cur & 1)
					cand.push_back(d);
				cur >>= 1;
			}

			vector <long double> prob(k+1);
			prob[0] = 1;
			vector <long double> temp(k+1);
			for (int d = 0; d < k; ++d) {
				for (int d1 = 0; d1 <= k; ++d1)
					temp[d1] = 0;
				for (int d1 = 0; d1 <= d; ++d1) {
					//long double a = prob[d1] * p[cand[d]];
					//long double b = prob[d1 + 1] * (1 - p[cand[d]]);
					temp[d1] += prob[d1] * (1 - p[cand[d]]);
					temp[d1 + 1] += prob[d1] * p[cand[d]];
					//temp[d1 + 1] = a + b;
				}

				prob = temp;
			}

			mx = max(mx, prob[k/2]);
		}
		cout << fixed << setprecision(8) << mx << endl;
	}
}