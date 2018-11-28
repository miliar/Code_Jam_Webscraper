#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	freopen("A-small-attempt0.in", "rb", stdin);
	freopen("trick.txt", "wb", stdout);

	int t, k = 0;
	scanf("%d", &t);
	while(k++ < t) 
	{
		int m, n;
		int arr1[4][4], arr2[4][4];
		scanf("%d", &m);
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				scanf("%d", &arr1[i][j]);

		scanf("%d", &n);
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				scanf("%d", &arr2[i][j]);

		int count = 0, flag;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(arr1[m-1][i] == arr2[n-1][j])
				{
					++count;
					flag = arr1[m-1][i];
				}

		if(count == 1)
			printf("Case #%d: %d\n", k, flag);
		else if(count == 0)
			printf("Case #%d: Volunteer cheated!\n", k);
		else
			printf("Case #%d: Bad magician!\n", k);
	}
	return 0;
}