#include<cstdlib>
#include<cstdio>
#include <iostream>
#include <iomanip>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int war(vector<double> v1, vector<double> v2) {
	int value = 0;
	for (int i = 0; i < v1.size(); i++) {
		for (int j = 0; j < v2.size(); j++) {

			if (v1[i] < v2[j]) {
				v2.erase(v2.begin() + j);
				break;
			}
			if (j == v2.size() - 1)
				value++;
		}
	}
	return value;
}

int dwar(vector<double> v1, vector<double> v2) {
	int value = 0;
	for (int i = v1.size() - 1; i >= 0; i--) {
		if (v1[i] > v2[v2.size() - 1]) {
			v2.erase(v2.begin() + (v2.size() - 1));
			v1.erase(v1.begin() + i);
			value++;
		} else {
			if (v1[0] < v2[v2.size() - 1]) {
				v2.erase(v2.begin() + (v2.size() - 1));
				v1.erase(v1.begin());
			}
		}
	}

	return v2.size() + value;
}
int main() {
	freopen("D-larg.out", "w", stdout);
	freopen("D-large.in", "r", stdin);
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; i++) {
		int mas;
		cin >> mas;
		vector<double> v1;
		vector<double> v2;
		for (int j = 0; j < mas; j++) {
			double m;
			cin >> m;
			v1.push_back(m);
		}

		for (int j = 0; j < mas; j++) {
			double m;
			cin >> m;
			v2.push_back(m);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		int value1 = war(v1, v2);
		int value2 = dwar(v1, v2);
		cout << "Case #" << i << ": " << value2 << " " << value1 << endl;
	}
	return 0;
}
