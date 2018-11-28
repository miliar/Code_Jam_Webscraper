#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int tests;
	cin >> tests;
	for(int caseNum = 1; caseNum <= tests; caseNum++) {
		int n;
		vector<double> naomi, ken;

		cin >> n;
		for(int i=0; i<n; i++) {
			double w; cin >> w;
			naomi.push_back(w);
		}
		for(int i=0; i<n; i++) {
			double w; cin >> w;
			ken.push_back(w);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int kenFirst, kenLast;

		int score1 = 0;
		kenFirst = 0, kenLast = n-1;
		for(int i=0; i<n; i++) {
			if(naomi[i] < ken[kenFirst]) {
				kenLast--;
			}
			else {
				score1++;
				kenFirst++;
			}
		}

		int score2 = n;
		kenFirst = 0, kenLast = n-1;
		for(int naoIdx = n-1; naoIdx >= 0; naoIdx--) {
			if(naomi[naoIdx] > ken[kenLast]) {
				kenFirst++;
			}else {
				kenLast--;
				score2--;
			}
		}

		cout << "Case #" << caseNum << ": ";
		cout << score1 << " " << score2 << endl;
	}
	return 0;
}