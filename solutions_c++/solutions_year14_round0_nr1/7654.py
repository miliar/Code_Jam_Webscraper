#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;
int T;
int ans1,ans2;
int a[5][5];
int b[5][5];
int main()
{	
	freopen("E:\\ACM  练习\\代码文件\\cao11\\cao11\\A-small-attempt1.in","r",stdin);
	freopen("E:\\ACM  练习\\代码文件\\cao11\\cao11\\result.out","w",stdout);
	scanf("%d",&T);
	int ca=0;
	while(T--)
		{
		ca++;
		scanf("%d",&ans1);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				{
				scanf("%d",&a[i][j]);
				}
		scanf("%d",&ans2);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				{
				scanf("%d",&b[i][j]);
				}
		int flag=0;
		int ans;
		for(int i=1;i<=4;i++)
			{
			for(int j=1;j<=4;j++)
				{
				if(a[ans1][i]==b[ans2][j])
					{
					if(flag==0)
						{
						flag=1;
						ans=a[ans1][i];
						}
					else if(flag==1)
						{
						flag=2;
						}
					}
				}
			}
		if(flag==0)
			{
			printf("Case #%d: Volunteer cheated!\n",ca);
			}
		else if(flag==1)
			{
			printf("Case #%d: %d\n",ca,ans);
			}
		else if(flag==2)
			{
			printf("Case #%d: Bad magician!\n",ca);
			}
	}
return 0;

}