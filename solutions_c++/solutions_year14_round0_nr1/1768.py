#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

int L, c[16], mark[20];

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("a_small.out", "w", stdout);
	int TT = 0, NumT;
	scanf("%d", &NumT);
	while (NumT--) {
		memset(mark, 0, sizeof(mark));
		for (int i = 0; i != 2; i++) {
			scanf("%d", &L);
			for (int k = 0; k != 16; k++) scanf("%d", &c[k]);
			for (int k = 0; k != 4; k++) mark[c[L * 4 - 4 + k]]++;
		}	
		int p = 0, num = 0;
		for (int i = 1; i <= 16; i++)
			if (mark[i] > 1) {
				p = i;
				num++;
			}
		printf("Case #%d: ", ++TT);
		if (num == 0) printf("Volunteer cheated!\n");
		else if (num > 1) printf("Bad magician!\n");
		else printf("%d\n", p);
	}
	return 0;
}