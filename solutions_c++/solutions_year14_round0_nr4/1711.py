#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
int main() {
	freopen("D-large.in", "r", stdin);
	freopen("Dout.txt", "w", stdout);
	int tc;
	cin >>tc;
	
	for (int q = 1; q <= tc; q++) {
		int n;
		cin >> n;
	//	double ken[1005], naomi[1005];
		vector<double> ken, naomi, dupken, dupnaomi;
		for (int i = 0; i < n; i++) {
			double temp;
			scanf("%lf", &temp);
			naomi.push_back(temp);
			dupnaomi.push_back(temp);
		}
		for (int i = 0; i < n; i++) {
			double temp;
			scanf("%lf", &temp);
			ken.push_back(temp);
			dupken.push_back(temp);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		sort(dupnaomi.begin(), dupnaomi.end());
		sort(dupken.begin(), dupken.end());
		int count = 0;
		int count2 = 0;
		//Deceitful simulation
		for (int i = 0; i < n; i++) {
			double kenno = ken[0];
			ken.erase(ken.begin());
			vector<double>::iterator naomipos = upper_bound(naomi.begin(), naomi.end(), kenno);
			if (naomipos == naomi.end()) {
				naomi.erase(naomi.begin());
			}
			else {
				naomi.erase(naomipos);
				count++;
			}
		}
		//War simulation
		for (int i = 0; i < n; i++) {
			double naomino = dupnaomi[0];
			dupnaomi.erase(dupnaomi.begin());
			vector<double>::iterator kenpos = upper_bound(dupken.begin(), dupken.end(), naomino);
			if (kenpos == dupken.end()) {
				dupken.erase(dupken.begin());
			}
			else {
				dupken.erase(kenpos);
				count2++;
			}
		}

		printf("Case #%d: %d %d\n", q, count,n-count2);
	}
}
