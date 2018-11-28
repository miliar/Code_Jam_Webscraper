#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#define SIZE(x) ((int)(x).size())
#define ALL(x) (x).begin(), (x).end()
#define REP(i,b) for(int i=0; i<(b); ++i)
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

using namespace std;
typedef vector<int> VI;
typedef long long LL;

int t;

void print(vector<double>& V) {
	for(auto x: V) cout << x << " ";
	cout << endl;
}

int main() {
	scanf("%d", &t);

	vector<double> naomi;
	vector<double> ken;

	REP(i,t) {
		int n;
		scanf("%d", &n);

		naomi.resize(n);
		ken.resize(n);

		REP(i,n) cin >> naomi[i];
		REP(i,n) cin >> ken[i];

		sort(ALL(naomi));
		sort(ALL(ken));

		set<double> ken_set, ken_set2;
		for(auto x: ken) ken_set.insert(x);

		int normal_war_points = 0, deceitful_war_points = 0;
		for(auto x: naomi) {
			set<double>::iterator upp = ken_set.upper_bound(x);
			if (upp == ken_set.end()) {
				ken_set.erase(ken_set.begin());
				normal_war_points++;
			} else ken_set.erase(upp);
			//cout << x << " - " << *upp << endl;
		}

		while(SIZE(naomi)>1) {
			//print(naomi);
			//print(ken);
			
			while(naomi.front() < ken.front()) {
				if (SIZE(naomi)<1) break;
				naomi.erase(naomi.begin());
				ken.erase(--ken.end());
			}

			//print(naomi);
			//print(ken);

			VI ids_to_save;
			REP(i,SIZE(naomi)) {
				if (naomi[i]>ken[i]) {
					deceitful_war_points++;
					ids_to_save.PB(i);
				} else break;
			}

			//print(naomi);
			//print(ken);

			sort(ALL(ids_to_save));
			reverse(ALL(ids_to_save));
			for(auto x: ids_to_save) {
				naomi.erase(naomi.begin()+x);
				ken.erase(ken.begin()+x);
			}

			//print(naomi);
			//print(ken);
		}

		//for(auto x: naomi) cout << x << " ";
		//cout << endl;

		//for(auto x: ken) cout << x << " ";
		//cout << endl;

		naomi.clear();
		ken.clear();


		deceitful_war_points = max(deceitful_war_points,normal_war_points);

		cout << "Case #" << i+1 << ": " << deceitful_war_points << " " << normal_war_points << endl;
	}

	return 0;
}
