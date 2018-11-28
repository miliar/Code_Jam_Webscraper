#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<double> ken, naomi;

int playwar() {
	vector<double> nao = naomi, ke = ken;
	int ret = 0;
	while (!nao.empty()) {
		double a = nao[0];
		nao.erase(nao.begin());
		int i = ke.size()-1;
		while (i > 0 && ke[i-1] > a) i--;
		if (ke[i] < a) ret++;
		ke.erase(ke.begin()+i);
	}
	return ret;
}

int playdeceitful() {
	vector<double> nao = naomi, ke = ken;
	int ret = 0;
	while (!nao.empty()) {
		if (nao.back() < ke.back()) {
			nao.erase(nao.begin());
		}
		else {
			nao.pop_back();
			ret++;
		}
		ke.pop_back();
	}
	return ret;
}

void solve(int cs) {
	scanf("%d", &n);
	ken.resize(n); naomi.resize(n);
	for (int i = 0; i < n; i++) scanf("%lf", &naomi[i]);
	for (int i = 0; i < n; i++) scanf("%lf", &ken[i]);
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	int z = playwar();
	int y = playdeceitful();
	printf("Case #%d: %d %d\n", cs, y, z);
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}