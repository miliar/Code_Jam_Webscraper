#include <deque>
#include <algorithm>
#include <iostream>
using namespace std;

typedef deque<double> dd;

dd naomiW, naomiDW, kenW, kenDW;
int war_score, dwar_score, T, N;
double aux;

int main() {
	ios_base::sync_with_stdio(false);
	
	cin >> T;
	for (int caso=1; caso<=T; caso++) {
		war_score = 0; dwar_score = 0;
		naomiW.clear(); kenW.clear();
		naomiDW.clear(); kenDW.clear();

		cin >> N;

		for (int i=0; i<N; i++) {
			cin >> aux;
			naomiW.push_back(aux);
		}

		for (int i=0; i<N; i++) {
			cin >> aux;
			kenW.push_back(aux);
		}

		sort(naomiW.begin(),naomiW.end());
		naomiDW = dd(naomiW.begin(), naomiW.end());
		sort(kenW.begin(),kenW.end());
		kenDW = dd(kenW.begin(), kenW.end());

		for (int i=0; i<N; i++) {
			double naomi = naomiW.front(); naomiW.pop_front();
			dd::iterator it = upper_bound(kenW.begin(), kenW.end(), naomi);
			if (it == kenW.end()) {
				kenW.pop_front();
				war_score++;
			} else {
				kenW.erase(it);
			}
		}

		for (int i=0; i<N; i++) {
			if (naomiDW.back() > kenDW.back()) {
				naomiDW.pop_back(); kenDW.pop_back();
				dwar_score++;
			} else {
				naomiDW.pop_front(); kenDW.pop_back();
			}
		}
		

		cout << "Case #" << caso << ": " << dwar_score << " " << war_score << "\n";
	}
}