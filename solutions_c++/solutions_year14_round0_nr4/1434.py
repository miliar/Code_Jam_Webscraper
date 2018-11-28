#include <iostream>
#include <vector>

using namespace std;

int calcWar(vector<double> naomi, vector<double> ken) {
	int k = 0;
	for (int i = 0; i < naomi.size(); i++) {
		for (vector<double>::iterator it = ken.begin(); it != ken.end(); ++it) {
			if (*it > naomi[i]) { //get onepoint
				ken.erase(it);
				k++;
				break;
			}
		}
	}
	return naomi.size() - k;
}

int deceitfulWar(vector<double> naomi, vector<double> ken) {
	int n = 0;
	for (int i = 0; i < naomi.size(); i++) {
		if (naomi[i] > ken[0]) {
			n++;
			ken.erase(ken.begin());
		} else {
			ken.erase(ken.end() - 1);
		}
	}
	return n;
}

int main() {
	int t = 0;
	cin >> t;
	int n = 0;
	for (int i = 0; i < t; i++) {
		cin >> n;
		vector<double> naomi(n, 0.0);
		for (int j = 0; j < n; j++)
			cin >> naomi[j];
		vector<double> ken(n, 0.0);
		for (int j = 0; j < n; j++)
			cin >> ken[j];

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int dw = deceitfulWar(naomi, ken);
		int w = calcWar(naomi, ken); //war
		cout << "Case #" << i + 1 << ": " << dw << " " << w << endl; 
	}
	return 0;
}