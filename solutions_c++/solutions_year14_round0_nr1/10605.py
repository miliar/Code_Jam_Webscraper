#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>


using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
	int i, temp, j, arr[20], tc, cs=1, n, con, ans;
	scanf("%d", &tc);
	while(tc--)
	{
		con=0;
		memset(arr, 0, sizeof(arr));
		scanf("%d", &temp);
		for(i=1; i<=4; i++)
		{
			for(j=1; j<=4; j++)
			{
				scanf("%d", &n);
				if(i==temp)
				arr[n]=1;
			}
		}


		scanf("%d", &temp);
		for(i=1; i<=4; i++)
		{
			for(j=1; j<=4; j++)
			{
				scanf("%d", &n);
				if(i==temp)
				{
					if(arr[n]==1)
					{
						con++;
						ans=n;
					}
				}
			}
		}
		if(con==1)
		printf("Case #%d: %d\n", cs++, ans);
		else if(con==0)
		printf("Case #%d: Volunteer cheated!\n", cs++);
		else
		printf("Case #%d: Bad magician!\n", cs++);
	}
	return 0;
}
