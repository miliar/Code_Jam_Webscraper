#include <bits/stdc++.h>

using namespace std;

int st[5][5];
int nd[5][5];

int main() {
	int n;
	scanf("%d", &n);
	int pri, seg, ind = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &pri);
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				scanf ("%d", &st[j][k]);
			}
		}
		
		scanf("%d", &seg);
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				scanf ("%d", &nd[j][k]);
			}
		}
		
		int conta = 0, ans = -1;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				if (st[pri-1][j] == nd[seg-1][k]) {
					++conta;
					ans = st[pri-1][j];
				}
			}
		}
		if(conta) {
			if(conta == 1) printf("Case #%d: %d\n", ++ind, ans);
			else  printf("Case #%d: Bad magician!\n", ++ind);
		} else printf("Case #%d: Volunteer cheated!\n", ++ind);
	}
	return 0;
}