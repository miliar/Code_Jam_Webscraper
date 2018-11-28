#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
	int cs, i, j, k, n,m;
	int arr[5][5], arr2[5][5];
	int xo[17];
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &cs);
	int tt = 0;
	while (cs--)
	{
		memset(xo, 0, sizeof(xo));
		scanf("%d", &n);
		--n;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &arr[i][j]);
			}
		for (int i = 0; i < 4; ++i)
			xo[arr[n][i]]++;
		scanf("%d", &n);
		--n;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &arr[i][j]);
			}
		for (int i = 0; i < 4; ++i)
			xo[arr[n][i]]++;
		n = 0;
		for (int i = 1; i <= 16 && n != -1; ++i)
		{
			if (xo[i] == 2)
			{
				if ( n != 0 )
				{
					n = -1;
				}
				else
				{
					n = i;
				}
			}
		}
		if (n > 0 )
			printf("Case #%d: %d\n", ++tt, n);
		else if ( n == -1)
			printf("Case #%d: Bad magician!\n", ++tt);
		else
			printf("Case #%d: Volunteer cheated!\n", ++tt);
	}
}
		
		
			
		
