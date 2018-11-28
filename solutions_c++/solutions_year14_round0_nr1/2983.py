#include <iostream>
#include <cstdio>
using namespace std;

int tn, r1, r2, i, j, x, kk[17], tt, lt, qt;

int main (int argc, char * const argv[]) {
	scanf("%d", &tn);
	while (tn--) {
		scanf("%d", &r1);
		for(i = 1; i <= 4; i++) for(j = 1; j <= 4; j++) {
			scanf("%d", &x);
			if (i == r1) ++kk[x];
		}
		scanf("%d", &r2);
		for(i = 1; i <= 4; i++) for(j = 1; j <= 4; j++) {
			scanf("%d", &x);
			if (i == r2) ++kk[x];
		}
		tt = lt = 0;
		for(i = 1; i <= 16; i++) {
			if (kk[i] == 2) ++tt, lt = i;
			kk[i] = 0;
		}
		++qt;
		if (tt > 1) printf("Case #%d: Bad magician!\n", qt); else
		if (tt == 0) printf("Case #%d: Volunteer cheated!\n", qt); else printf("Case #%d: %d\n", qt, lt);		
	}
    return 0;
}
