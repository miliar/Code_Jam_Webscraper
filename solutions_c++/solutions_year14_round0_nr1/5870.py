#include <bits/stdc++.h>
using namespace std;

int a[4][4], r1[4], r2[4];

int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; ++tt)
	{
		int x;
		scanf("%d", &x);
		--x;
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j) scanf("%d", &a[i][j]);
		for(int i = 0; i < 4; ++i) r1[i] = a[x][i];
		int y;
		scanf("%d", &y);
		--y;
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j) scanf("%d", &a[i][j]);
		for(int i = 0; i < 4; ++i) r2[i] = a[y][i];
		int count = 0, result;
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j) if(r1[i] == r2[j]) ++count, result = r1[i];
		if(!count) printf("Case #%d: Volunteer cheated!\n", tt);
		else if (count > 1) printf("Case #%d: Bad magician!\n", tt);
		else printf("Case #%d: %d\n", tt, result);
	}
	return 0;
}