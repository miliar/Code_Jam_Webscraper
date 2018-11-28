#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void solve()
{
	int n;

	vector<double> naomi;
	vector<double> ken;

	vector<double> naomi2;
	vector<double> ken2;

	cin >> n;
	double x;
	for(int i = 0; i < n; ++i) {
		cin >> x;
		naomi.push_back(x);
	}

	for(int i = 0; i < n; ++i) {
		cin >> x;
		ken.push_back(x);
	}
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());

	naomi2 = naomi;
	ken2 = ken;

	int deceitful = 0;

	// deceitful
	for(int i = 0; i < naomi.size(); ++i) {
		double cur_block = naomi[i];
		if(cur_block > ken[0]) {
			++deceitful;
			ken.erase(ken.begin());
		}
		else {
			ken.pop_back();
		}
	}
	cout << deceitful << " ";

	// normal

	int optimal = 0;

	for(int i = 0; i < naomi2.size(); ++i) {
		double cur_block = naomi2[i];
		if (ken2.back() < cur_block) {
			++optimal;
			ken2.erase(ken2.begin());
		}
		else {
			for(int j = 0; j < ken2.size(); ++j) {
				if(ken2[j] > cur_block) {
					ken2.erase(ken2.begin()+j);
					break;
				}
			}
		}
	}
	cout << optimal << endl;

}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}