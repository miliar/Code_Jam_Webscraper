#include <cstdio>
#include <set>
#include <algorithm>

using namespace std;
int a[4][4];

int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		set<int> S; printf("Case #%d: ", _);
		int t; scanf("%d", &t); t--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) scanf("%d", &a[i][j]);
		for (int i = 0; i < 4; i++) S.insert(a[t][i]);
		scanf("%d", &t); t--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) scanf("%d", &a[i][j]);
		int cnt = 0, Ans = -1;
		for (int i = 0; i < 4; i++) {
			if (S.find(a[t][i]) != S.end()) cnt++, Ans = a[t][i];
		}
		if (cnt == 1) printf("%d\n", Ans);
		else if (cnt == 0) puts("Volunteer cheated!");
		else if (cnt > 1) puts("Bad magician!");
	}
}

