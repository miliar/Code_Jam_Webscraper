#include <cstdio>
#include <algorithm>

int m[5][5];
bool num[2][20];

int main()
{
	int caseT,a1,a2,ans;
	scanf("%d",&caseT);
	for(int casenum=1;casenum<=caseT;casenum++)
	{
		printf("Case #%d: ",casenum);
		std::fill(num[0],num[2],0);
		scanf("%d",&a1);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&m[i][j]);
		for(int i=1;i<=4;i++)
			num[0][m[a1][i]]=1;
		scanf("%d",&a2);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&m[i][j]);
		for(int i=1;i<=4;i++)
			num[1][m[a2][i]]=1;
		ans=-1;
		for(int i=1;i<=16;i++)
			if(num[0][i]&&num[1][i])
			{
				if(ans!=-1)
					ans=-2;
				else
					ans=i;
			}
		if(ans==-2)
			puts("Bad magician!");
		else if(ans==-1)
			puts("Volunteer cheated!");
		else
			printf("%d\n",ans);
	}
	return 0;
}
