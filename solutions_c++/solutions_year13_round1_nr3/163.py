#include <cstdio>
#include <vector>

using namespace std;

int r, n, m, k;

int prod[11];
bool multi[256];
vector<int> out;
vector<int> trial;

void genProd(int at=0) {
	if (out.size()) return;
	if (at == n) {
		// test
		for (int i=2; i<256; i++) {
			multi[i] = false;
		}
		for (int i=1; i<(1<<n); i++) {
			int cur = 1;
			for (int j=0; j<trial.size(); j++) {
				if (1<<j & i) {
					cur *= trial[j];
				}
			}
			multi[cur] = true;
		}
		bool all = true;
		for (int i=0; i<k; i++) {
			if (!multi[prod[i]]) all = false;
		}
		if (all) {
			for (int i=0; i<trial.size(); i++) {
				out.push_back(trial[i]);
			}
		}
	}
	else {
		for (int i=2; i<=m; i++) {
			trial.push_back(i);
			genProd(at+1);
			trial.pop_back();
		}
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%*d");
	printf("Case #1:\n");
	multi[1] = true;
	scanf("%d%d%d%d", &r, &n, &m, &k);
	for (int i=0; i<r; i++) {
		for (int j=0; j<k; j++) {
			scanf("%d", &prod[j]);
		}
		out.clear();
		genProd();
		for (int i=0; i<out.size(); i++) {
			printf("%d", out[i]);
		}
		printf("\n");
	}
	return 0;
}