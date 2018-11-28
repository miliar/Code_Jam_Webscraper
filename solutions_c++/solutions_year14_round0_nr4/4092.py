#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>


using namespace std;

int main() {
	if(fopen("mine.in","r")) {
		freopen("mine.in","r",stdin);
		freopen("mine.out","w",stdout);
	}
	int t;
	int pointdec = 0;
	int pointtrue = 0;
	vector<double> naomi;
	vector<double> ken;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		pointdec = 0;
		pointtrue = 0;
		cout << "Case #";
		cout << i; 
		cout << ": ";
		int n;
		cin >> n;
		naomi.clear();
		ken.clear();
		for(int j = 1; j <= n; j++) {
			double a;
			cin >> a;
			naomi.push_back(a);
		}
		for(int j = 1; j <= n; j++) {
			double a;
			cin >> a;
			ken.push_back(a);
		}

		vector<double> naomiwork;
		vector<double> kenwork;
		naomiwork = naomi;
		kenwork = ken;
		sort(naomiwork.begin(), naomiwork.end());
		sort(kenwork.begin(), kenwork.end());
		bool realtalk = false;

		while(!realtalk && !naomiwork.empty()) {
			realtalk = true;
			for(int i = 0; i < naomiwork.size(); i++) {
				if(kenwork[i] > naomiwork[i]) {
					realtalk = false;
				}
			}
			
			if(realtalk) {
				pointdec = naomiwork.size();
				break;
			}
			else {
				naomiwork.erase(naomiwork.begin());
				kenwork.erase(kenwork.begin()+kenwork.size()-1);
			}
		}
		
		naomiwork = naomi;
		kenwork = ken;
		sort(naomiwork.begin(), naomiwork.end());
		sort(kenwork.begin(), kenwork.end());
		realtalk = false;
		int kenvalue;
		while(!naomiwork.empty()) {
			realtalk = true;
			
			for(int i = 0; i < kenwork.size(); i++) {
				if(naomiwork[0] < kenwork[i]) {
					kenvalue = kenwork[i];
					naomiwork.erase(naomiwork.begin());
					kenwork.erase(kenwork.begin()+i);
					realtalk = false;
					break;
				}
			}
			if(realtalk == true) {
				pointtrue++;
				naomiwork.erase(naomiwork.begin());
				kenwork.erase(kenwork.begin());
			}
		}
		cout << pointdec << ' ' << pointtrue << '\n';
	}
	return 0;
}