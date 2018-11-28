#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;
int casenum,T;

int main() {
	freopen("gcj14.in","r",stdin);
	freopen("gcj14.out","w",stdout);
	cin >> T;
	for (casenum = 1; casenum <= T; casenum++) {
		cout << "Case #" << casenum << ": ";
		int n;
		cin >> n;
		vector<double> naomi;
		vector<double> ken;
		naomi.clear();
		ken.clear();
		for (int i = 0; i < n; i++) {
			double x;
			cin >> x;
			naomi.push_back(x);
		}
		for (int i = 0; i < n; i++) {
			double x;
			cin >> x;
			ken.push_back(x);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int y = 0;
		int z = n;
		int i = 0;
		int j = 0;
		while (i < n) {
			if (naomi[i] > ken[j]) {
				j++;
				y++;
			}
			i++;
		}
		i = j = 0;
		while (i < n) {
			while (j < n && naomi[i] > ken[j])
				j++;
			if (j == n)
				break;
			z--;
			i++;
			j++;
		}
		cout << y << " " << z;
		cout << endl;
	}
	return 0;
}
