#include <stdio.h>
#include <string.h>

int main()
{
	int T, xx = 0;
	int fir, sec, count, num;
	int i, j, k = 0;
	int a[4][4], b[4][4];
	int ans[100];
	memset(ans, 0, sizeof(ans));
	

	scanf("%d", &T);

	while (T-- > 0)
	{
		count = 0, num = 0;
		scanf("%d", &fir);
		for(i = 0; i <= 3; i++)
		{
			scanf("%d %d %d %d", &a[i][0], &a[i][1], &a[i][2], &a[i][3] );
		}
		
		scanf("%d", &sec);
		for(i = 0; i <= 3; i++)
		{
			scanf("%d %d %d %d", &b[i][0], &b[i][1], &b[i][2], &b[i][3] );
		}
		

		for(i = 0; i <= 3; i++)
			for(j = 0; j <= 3; j++)
			{
				if (a[(fir - 1)][i] == b[(sec - 1)][j])
				{
					++count;
					num = a[(fir - 1)][i];
				}

			}
			switch (count)
			{
				case 0:				
					printf("Case #%d: Volunteer cheated!\n", ++xx);
					break;
				case 1:
					printf("Case #%d: %d\n", ++xx, num);
					break;
				default:
					printf("Case #%d: Bad magician!\n", ++xx);
					
			
			}
			
				
		/*
		if (count > 1)
		{
			ans[++k] = 2;
		}
		else if (count == 0)
		{
			ans[++k] = 3;
		}
		else
			ans[++k] = 1;
	

	}
    for (i = 1; i <= k; i++)
    {
		if (ans[1] == )
		{
		} 
		else
		{
		}
		
    }
	*/
	}
	return 0;


}