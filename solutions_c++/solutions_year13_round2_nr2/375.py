#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
const int N = 105;
typedef __int64 ll;
int a[N];
double dp[25][25][25];
int main()
{
	int T,x,y,n,ca=1,i;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		double r=0.0;
		scanf("%d%d%d",&n,&x,&y);
		if(x<0)x=-x;
		int pre=0,cnt=1,d=1,k=5;
		for(;cnt<n;d++,k+=4)
		{
			pre=cnt;
			cnt+=k;
		}
		int dep=(x+y)/2+1;
		if(dep>d)r=0.0;
		else if(dep<d)r=1.0;
		else if(dep==d&&cnt==n)r=1.0;
		else if(dep==d&&x==0)r=0.0;
		else
		{
			//puts("what");
			memset(dp,0,sizeof(dp));
			int m=n-pre,rd=d*2-1,j,h;
			//printf("m:%d rd:%d \n",m,rd);
			dp[0][0][0]=1.0;
			for(i=1;i<=m;i++)
			{
				for(j=0;j<rd;j++)
				{
					for(h=0;h<rd;h++)
					{
						double v=dp[i-1][j][h];
						if(j==rd-1)dp[i][j][h+1]+=v;
						else if(h==rd-1)dp[i][j+1][h]+=v;
						else
						{
							dp[i][j+1][h]+=0.5*v;
							dp[i][j][h+1]+=0.5*v;
						}
					}
				}
			}
			r=0.0;
			for(i=y+1;i<rd&&i<=m;i++)r+=dp[m][m-i][i];
		}
		printf("Case #%d: %.9lf\n",ca++,r);
	}
	return 0;
}