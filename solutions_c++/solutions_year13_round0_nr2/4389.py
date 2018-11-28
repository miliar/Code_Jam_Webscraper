#include<stdio.h>
#include<string.h>

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, Case = 1;
	int n, m, i, j;
	int a[105][105];
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d", &n, &m);
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				scanf("%d", &a[i][j]);
			}
		}

		int ok, x, y, sideok, res=1;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				ok = 2;

				//ºá
				sideok=2;
				x=i;
				y=j-1;
				while(y>=0)
				{
					if(a[x][y]>a[i][j])
					{
						sideok--;
						break;
					}
					y--;
				}
				y=j+1;
				while(y<m)
				{
					if(a[x][y]>a[i][j])
					{
						sideok--;
						break;
					}
					y++;
				}
				if(sideok<2) ok--;

				//Êú
				sideok=2;
				x=i-1;
				y=j;
				while(x>=0)
				{
					if(a[x][y]>a[i][j])
					{
						sideok--;
						break;
					}
					x--;
				}
				x=i+1;
				while(x<n)
				{
					if(a[x][y]>a[i][j])
					{
						sideok--;
						break;
					}
					x++;
				}
				if(sideok<2) ok--;
				
				if(ok<1)
				{
					res = 0;
					break;
				}
			}
			if(res == 0 ) break;
		}
		if(res == 1) printf("Case #%d: YES\n", Case++);
		else printf("Case #%d: NO\n", Case++);
	}
	return 0;
}