#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int count = 1; count <= T; count++) {
		int n;
		cin >> n;
		vector<double> naomi(n);
		vector<double> ken(n);
		for(int i = 0; i < n; i++) cin >> naomi[i];
		for(int i = 0; i < n; i++) cin >> ken[i];
		sort(naomi.begin(), naomi.end(), greater<double>());
		sort(ken.begin(), ken.end(), greater<double>());
		vector<double> naomi2(naomi);
		vector<double> ken2(ken);
		int pnaomi1 = 0, pnaomi2 = 0;
		for(int play = 0; play < n; play++) {
			if(ken[0] > naomi[0]) {
				ken.erase(ken.begin());
				naomi.erase(--naomi.end());
			} else {
				pnaomi1++;
				ken.erase(ken.begin());
				naomi.erase(naomi.begin());
			}
		}
		naomi.assign(naomi2.begin(), naomi2.end());
		ken.assign(ken2.begin(), ken2.end());
		for(int play = 0; play < n; play++) {
			int i;
			for(i = n-1-play; i >= 0; i--) if(ken[i] > naomi.front()) break;
			if(i == -1) {
				pnaomi2++;
				naomi.erase(naomi.begin());
				ken.erase(--ken.end());
			} else {
				naomi.erase(naomi.begin());
				ken.erase(ken.begin()+i);
			}
		}
		cout << "Case #" << count << ": " << pnaomi1 << " " << pnaomi2 << endl;
	}
}
