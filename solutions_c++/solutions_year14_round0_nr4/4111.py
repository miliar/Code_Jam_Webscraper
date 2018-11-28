#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <bitset>
#include <algorithm>
#include <cstring>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define rtrav(it, v) for(typeof((v).rbegin()) it = (v).rbegin(); it != (v).rend(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int optimal_war(const set<double> &naomi, set<double> ken) {
	int v = 0;
	trav(nit, naomi) {
		set<double>::iterator kit = ken.upper_bound(*nit);
		if (kit == ken.end()) {
			++v;
			ken.erase(ken.begin());
		} else {
			ken.erase(kit);
		}
	}
	return v;
}

int optimal_deceitful_war(set<double> naomi, set<double> ken) {
	int v = 0;

	while(!naomi.empty()) {
		set<double>::reverse_iterator nit = naomi.rbegin();
		set<double>::iterator kit = ken.upper_bound(*nit);
		if (kit == ken.end()) {
			++v;
			naomi.erase(naomi.upper_bound(*ken.begin()));
			ken.erase(ken.begin());
		} else {
			ken.erase(kit);
			naomi.erase(naomi.begin());
		}
	}

	return v;
}

int main(int argc, char const *argv[]) {
	int T, N;
	double tmp;
	scanf("%d", &T);
	rep(t, 0, T) {
		scanf("%d", &N);
		set<double> naomi, ken;
		rep(n, 0, N) {
			scanf("%lf", &tmp);
			naomi.insert(tmp);
		}
		rep(n, 0, N) {
			scanf("%lf", &tmp);
			ken.insert(tmp);
		}
		printf("Case #%d: %d %d\n", t+1, optimal_deceitful_war(naomi, ken), optimal_war(naomi, ken));
	}
	return 0;
}