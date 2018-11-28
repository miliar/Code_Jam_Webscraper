#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>

using namespace std;

const int MAXN = 1002;

int N;
set<double> naomiWar;
set<double> naomiDWar;
set<double> kenWar;
set<double> kenDWar;

int main(void) {
	double temp;
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%d", &N);
		for(int i = 0; i < N; i++){ 
			scanf("%lf", &temp);
			naomiWar.insert(temp);
			naomiDWar.insert(temp);
		}

		for(int i = 0; i < N; i++){ 
			scanf("%lf", &temp);
			kenWar.insert(temp);
			kenDWar.insert(temp);
		}

		int resW = 0, resDW = 0;
		for(int k = 0; k < N; k++) {
			set<double>::iterator kenDStart = kenDWar.begin();
			set<double>::iterator kenDEnd = kenDWar.end(); kenDEnd--;

			set<double>::iterator kenStart = kenWar.begin();
			set<double>::iterator kenEnd = kenWar.end(); kenEnd--;

			set<double>::iterator naomiDStart = naomiDWar.begin();
			set<double>::iterator naomiDEnd = naomiDWar.end(); naomiDEnd--;

			set<double>::iterator naomiStart = naomiWar.begin();
			set<double>::iterator naomiEnd = naomiWar.end(); naomiEnd--;

			//printf("%lf %lf\n", *naomiEnd, *kenEnd);

			if(*naomiEnd > *kenEnd) {
				naomiWar.erase(naomiEnd);
				kenWar.erase(kenStart);
				resW++;
			} else {
				naomiWar.erase(naomiEnd);
				kenWar.erase(kenEnd);
			}

			if(*naomiDEnd > *kenDEnd) {
				naomiDWar.erase(naomiDWar.upper_bound(*kenDStart));
				kenDWar.erase(kenDStart);
				resDW++;
			} else {
				naomiDWar.erase(naomiDStart);
				kenDWar.erase(kenDEnd);
			}
		}

		printf("Case #%d: %d %d\n", t, resDW, resW);

		naomiWar.clear(); naomiDWar.clear();
		kenWar.clear(); kenDWar.clear();
	}
	return 0;
}
