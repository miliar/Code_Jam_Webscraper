#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

#define EPSILON		0.0000001

using namespace std;

bool check(vector<double> a, vector<double> b) {
	int i;
	
	for (i = 0; i < (int)a.size(); i++) {
		if (a[i] < b[i]) return false;
	}
	
	return true;
}

void solve() {
	int n;
	int i;
	vector<double> naomi, ken2;
	set<double> ken;
	double a;
	int war = 0;
	
	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> a;
		naomi.push_back(a);
	}
	for (i = 0; i < n; i++) {
		cin >> a;
		ken.insert(a);
		ken2.push_back(a);
	}
	
	sort(naomi.begin(), naomi.end());
	sort(ken2.begin(), ken2.end());
	
	for (i = 0; i < (int)naomi.size(); i++) {
		double na = naomi[naomi.size() - 1 - i];
		set<double>::iterator ke = ken.upper_bound(na);
		
		if (ke == ken.end()) {
			war++;
			ken.erase(ken.begin());
		} else {
			ken.erase(ke);
		}
	}
	
	while (!check(naomi, ken2)) {
		naomi.erase(naomi.begin());
		ken2.pop_back();
	}
	
	cout << naomi.size() << " " << war;
}

int main() {
	int cases;
	int i;
	
	cin >> cases;
	for (i = 1; i <= cases; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	
	return 0;
}