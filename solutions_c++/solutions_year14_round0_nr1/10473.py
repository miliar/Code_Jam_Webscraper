#include<cstdio>

int main()
{
	int a[4][4], a1[4], a2[4];
	int i, j, k, t, m, n, count = 0, ans;
	
	scanf("%d", &t);
	for(i = 0; i < t; i++) {
		scanf("%d", &m);
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				scanf("%d", &a[j][k]);
		for(k = 0; k < 4; k++)
			a1[k] = a[m-1][k];
		scanf("%d", &n);
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				scanf("%d", &a[j][k]);
		for(k = 0; k < 4; k++)
			a2[k] = a[n-1][k];
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				if(a1[j] == a2[k]) {
					count++;
					ans = a1[j];
				}
		if(count == 1)
			printf("Case #%d: %d\n", i+1, ans);
		if(count > 1)
			printf("Case #%d: Bad magician!\n", i+1);
		if(count == 0)
			printf("Case #%d: Volunteer cheated!\n", i+1);
		count = 0;
	}
	return 0;
}
