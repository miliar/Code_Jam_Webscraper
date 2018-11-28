#include <cstdio>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

long long FAT = 1000002013;

struct event {
	long long date;
	bool entre;
	bool operator<(const event& a) const {
		return (date < a.date) || (date == a.date && entre > a.entre);
	}
};

long long cout(long long k, long long stations) {
	return ((k*(2*stations - k +1))/2)%FAT;
}

int main(void) {
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		int voyages;
		long long stations;
		long long coutMax = 0, coutMin = 0;
		stack<long long> cartes;
		vector<event> evs;
		scanf("%lld%d", &stations, &voyages);
		for (int iVoy = 0; iVoy < voyages; iVoy++) {
			long long deb, fin;
			int fois;
			scanf("%lld%lld%d", &deb, &fin, &fois);
			event entrer, sort;
			entrer.date = deb, entrer.entre = true;
			sort.date = fin, sort.entre = false;
			for (int i = 0; i < fois; i++) {
				evs.push_back(entrer);
				evs.push_back(sort);
				coutMax = (coutMax+cout(fin-deb, stations))%FAT;
			}
		}
		sort(evs.begin(), evs.end());
		for (int iEv = 0; iEv < evs.size(); iEv++) {
			if (evs[iEv].entre)
				cartes.push(evs[iEv].date);
			else {
				long long cour = cartes.top();
				cartes.pop();
				coutMin = (coutMin+cout(evs[iEv].date-cour, stations))%FAT;
			}
		}
		printf("Case #%d: %lld\n", test, (coutMax-coutMin)%FAT);
	}
	return 0;
}
