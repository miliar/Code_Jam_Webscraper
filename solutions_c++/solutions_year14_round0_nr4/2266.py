#include <algorithm>
#include <cstdio>
#include <iostream>
#include <set>
#include <vector>

#define LOCAL_DEBUG

using namespace std;

int N;
vector<double> NAO, KEN;

void init() {
	NAO.clear();
	KEN.clear();
}

int playDeceitfulWar() {
	sort(KEN.begin(), KEN.end());
	int minBlock = KEN[0];
	int numGiveup = 0;
	for (int i = 0; i < N; i++)
		if (NAO[i] < minBlock)
			numGiveup++;
	set<double> nao;
	for (int i = numGiveup; i < N; i++)
		nao.insert(NAO[i]);
	int ret = 0;
	set<double>::iterator it;
	for (int i = 0; i < N-numGiveup; i++) {
		double ken = KEN[i];
		it = nao.lower_bound(ken);
		if (it != nao.end()) {
			ret++;
			nao.erase(it);
		} else break;
	}
	return ret;
}


int playWar() {
	sort(NAO.begin(), NAO.end());
	set<double> ken;
	for (int i = 0; i < N; i++)
		ken.insert(KEN[i]);
	int ret = 0;
	set<double>::iterator it;
	for (int i = 0; i < N; i++) {
		double nao = NAO[i];
		it = ken.lower_bound(nao);
		if (it != ken.end()) ken.erase(it);
		else { ret++; it--; ken.erase(it); }
	}
	return ret;
}

pair<int,int> solve() {
	return make_pair(playDeceitfulWar(), playWar());	
}

int main() {
#ifdef LOCAL_DEBUG
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
#endif
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		init();
		scanf("%d", &N);
		double block;
		for (int i = 0; i < N; i++) {
			scanf("%lf", &block);
			NAO.push_back(block);
		}
		for (int i = 0; i < N; i++) {
			scanf("%lf", &block);
			KEN.push_back(block);
		}
		pair<int,int> ans = solve();
		printf("Case #%d: %d %d\n", t, ans.first, ans.second);
	}
	return 0;
}