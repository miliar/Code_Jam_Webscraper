#include <cstdio>
using namespace std;
int nCases, tablea[4][4], tableb[4][4], rowa, rowb;
int possibility[4], nposs;
int main()
{
	scanf("%d", &nCases);
	for (int c = 0; c < nCases; c++) {
		scanf("%d", &rowa);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf(" %d", &tablea[i][j]);
			}
		}
		scanf("%d", &rowb);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf(" %d", &tableb[i][j]);
			}
		}
		for (int i = 0; i < 4; i++) {
			int current = tablea[rowa-1][i];
			for (int j = 0; j < 4; j++) {
				if (current == tableb[rowb-1][j]) {
					possibility[nposs] = current;
					nposs++;
				}
			}
		}
		printf("Case #%d: ", c+1);
		if (nposs == 0) printf("Volunteer cheated!\n");
		if (nposs > 1) printf("Bad magician!\n");
		if (nposs == 1) printf("%d\n", possibility[0]);
		possibility[0] = -1;
		nposs = 0;
	}
	return 0;
}
