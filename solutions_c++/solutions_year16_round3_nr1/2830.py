#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;

typedef unsigned long long ull;
#define forn(i, n) for(int i = 0; i < (int) n; i++)
#define forn1(i, n) for(int i = 1; i <= (int) n; i++)

bool isValid(const vector<int>& v, int num) {
	forn(i, v.size()) if (v[i] >= (num/2)+1) return false;
	return true;
}

int main() {
	int tn;
	cin >> tn;
	forn1(t, tn) {
		int n;
		cin >> n;
		vector<int> np(n);
		forn(i, n) cin >> np[i];
		int nir = 0;
		forn(i, n) nir += np[i];
		vector<int> npt(n);
		vector<string> ans;
		while (nir > 0) {
			string plan = "";
			forn(i, n) {
				forn(k, n) npt[k] = np[k];
				bool valPlan = false;
				if (np[i] == 0) continue;
				for(int j = i; j < n; j++) {
					if (np[j] == 0) continue;
					if (np[i] == 1 && i == j) continue;
					if (nir == 3) break;
					npt[i] -= 1;
					npt[j] -= 1;
					valPlan = isValid(npt, nir-2);
					/*
					cout << i << " " << j << " " << nir << " " << valPlan << endl;
					forn(k, n) cout << np[k] << " ";
					cout << endl;
					forn(k, n) cout << npt[k] << " ";
					cout << endl;
					cout << endl;
					*/
					if (valPlan) {
						np[i] -= 1;
						np[j] -= 1;
						nir -= 2;
						plan.push_back(i + 'A');
						plan.push_back(j + 'A');
						// cout << plan << endl;
						break;
					}
					npt[i] += 1;
					npt[j] += 1;
				}
				if (valPlan) break;
				else {
					npt[i] -= 1;
					if (isValid(npt, nir-1)) {
						np[i] -= 1;
						nir -= 1;
						plan.push_back(i + 'A');
						// cout << plan << endl;
						break;
					}
					npt[i] += 1;
				}
			}
			ans.push_back(plan);
		}
		cout << "Case #" << t << ": ";
		forn(i, ans.size()) cout << ans[i] << " ";
		cout << endl;
	}

	return 0;
}