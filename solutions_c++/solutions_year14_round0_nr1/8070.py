#include <stdio.h>
#include <set>
using namespace std;


int main () {
	int T, ma[5][5], row, gar,count = 1;
	scanf("%d", &T);
	while(T--) {
		set <int> S;
		scanf("%d", &row);

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &gar);
				if (i == row -1)
					S.insert(gar);
			}
		}
		int ANS = 0, nANS;
		scanf("%d", &row);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &gar);
				if (i == row - 1) {
					if (S.find(gar) != S.end()) {
						ANS++;
						nANS = gar;
					}
				}
			}
		}
		printf("Case #%d: ", count++);
		if (ANS == 0) printf("Volunteer cheated!\n");
		if (ANS == 1) printf("%d\n", nANS);
		if (ANS > 1) printf("Bad magician!\n");
	}
	return 0;
}