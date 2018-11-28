
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

typedef long long i8;

int tst;
int bo[4][4];

void solve() {
	int r1, r2, a=0, x, re;
	scanf("%d",&r1); --r1;
	for (int r=0; r<4; r++)
		for (int c=0; c<4; c++)
			scanf("%d", bo[r]+c);
	scanf("%d",&r2); --r2;
	for (int r=0; r<4; r++)
		for (int c=0; c<4; c++) {
			scanf("%d", &x);
			if (r==r2)
				for (int m=0; m<4; m++)
					if (bo[r1][m]==x) {
						a++;
						re=x;
					}
		}
		
	if (a==0) printf("Volunteer cheated!\n");
	if (a==1) printf("%d\n", re);
	if (a>=2) printf("Bad magician!\n");
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		printf("Case #%d: ", cas);
		solve();
	}
}
