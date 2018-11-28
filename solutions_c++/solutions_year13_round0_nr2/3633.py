#include<cstdio>
#include<iostream>

int main()
{
//	freopen("a.in", "r", stdin);
//	freopen("a.out", "w", stdout);
	int round;
	int check[105][2];
	int data[105][105];
	scanf("%d", &round);
	for(int i = 1;i <= round;i++){
		bool cancut = true;
		memset(check, 0, sizeof(check));
		int xx, yy;
		scanf("%d %d", &xx, &yy);
//		printf("%d %d\n", xx, yy);
		
		for(int j = 0;j < xx; j++)
			for(int k = 0;k < yy;k++)
				scanf("%d", &data[j][k]);
		for(int j = 0;j < xx;j++)
			for(int k = 0;k < yy;k++)
				if(check[j][0] < data[j][k])
					check[j][0] = data[j][k];
		for(int k = 0; k < yy; k++)
			for(int j = 0; j < xx; j++)
				if(check[k][1] < data[j][k])
					check[k][1] = data[j][k];
		for(int j = 0;j < xx; j++)
			for(int k = 0;k < yy;k++)
				if(data[j][k] < check[j][0] && data[j][k] < check[k][1])
					cancut = false;
/*		for(int j = 0;j < xx; j++)
			printf("%d ", check[j][0]);
		printf("\n");
		for(int j = 0;j < yy; j++)
			printf("%d ", check[j][1]);
		printf("\n");
*/		if(cancut)
			printf("Case #%d: YES\n", i);
		else
			printf("Case #%d: NO\n", i);
	}
	return 0;
}
