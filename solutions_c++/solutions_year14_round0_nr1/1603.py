#include<cstdio>
using namespace std;

int t, c=1;
int a, b, i, j;
int card1[4][4], card2[4][4];
int ticking[16];

int main() {
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	for (scanf("%d",&t); c<=t;++c) {
		scanf("%d", &a);
		for (i=0; i<4; ++i)
			for (j=0; j<4; ++j)
				scanf("%d", &card1[i][j]);
		scanf("%d", &b);
		for (i=0; i<4; ++i)
			for (j=0; j<4; ++j)
				scanf("%d", &card2[i][j]);
		--a; --b;
		for (i=0; i<4; ++i)
			ticking[card1[a][i]] = 0;
		for (i=0; i<4; ++i)
			++ticking[card2[b][i]];
		int ans = 0, repeat = 0;
		for (i=0; i<4; ++i)
			if (ticking[card1[a][i]])
				ans = card1[a][i], ++repeat;
		printf("Case #%d: ", c);
		if (repeat > 1)
			printf("Bad magician!\n");
		else if (ans)
			printf("%d\n", ans);
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}