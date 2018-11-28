#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

long double compute(vector<long double>& p) {
	int m = p.size();
	vector<long double> pr;
	pr.resize(m);
	pr[0] = 1 - p[0];
	pr[1] = p[0];
	for(int i = 1; i < p.size(); i++) {
		vector<long double> new_pr;
		new_pr.resize(m);
		for(int j = 0; j < m; j++) {
			new_pr[j] = pr[j] * (1 - p[i]);
		}
		for(int j = 1; j < m; j++) {
			new_pr[j] += pr[j - 1] * p[i];
		}
		pr.swap(new_pr);
	}
	return pr[m / 2];
}

int main(int argc, char** argv) {
	int t;
	cin >> t;
	for(int iter = 0; iter < t; iter++) {
		int n, m;
		cin >> n >> m;
		vector<long double> p;
		p.resize(n);
		for(int i = 0; i < n; i++) {
			cin >> p[i];
		}
		sort(p.begin(), p.end());

		double max_p = 0;
		for(int i = 0; i <= m; i++) {
			vector<long double> selected;
			for(int j = 0; j < i; j++) {
				selected.push_back(p[j]);
			}
			for(int j = n - 1; j >= 0; j--) {
				if(selected.size() >= m) break;
				selected.push_back(p[j]);
			}
			long double tie_p = compute(selected);
			if(tie_p > max_p) {
				max_p = tie_p;
			}
		}

		cout << "Case #" << iter + 1 << ": " << max_p << endl;
	}
	return 0;
}
