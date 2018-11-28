#pragma warning (disable: 4786)
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<math.h>
#include<ctype.h>
#include<algorithm>
#include<map>
#include<queue>
#include<vector>
#define INF 1<<29
using namespace std;
int main()
{
	//freopen("pp.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int  t1,i, j, k, t,r1, r2,first[6][6], second[6][6], select[6], flag[20];
	scanf("%d", &t);
	for( t1=1;t1<=t;t1++)
	{
		memset(flag, 0, sizeof(flag));
		scanf("%d", &r1);

		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d", &first[i][j]);
				if(i==r1)
				{
					select[j]=first[i][j];
					flag[select[j]]=1;
				}
			}
		}

		scanf("%d", &r2);

		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d", &second[i][j]);
			}
		}

		int ct=0, res;
		i=r2;
		for(j=1;j<=4;j++)
		{
			if(flag[second[i][j]]==1)
			{
				ct++;
				res=second[i][j];
			}
		}

		if(ct==1)
			printf("Case #%d: %d\n", t1,res );
		else if(ct==0)
			printf("Case #%d: Volunteer cheated!\n", t1);
		else if(ct>1)
			printf("Case #%d: Bad magician!\n", t1);
	}
	return 0;
}


