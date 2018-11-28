#include<iostream>
#include<map>
using namespace std;
int rec1[4][4];
int rec2[4][4];
double dp[2];
int main()
{
	int n;
	freopen("F://B-small-attempt1.in","r",stdin);
	freopen("F://out2.txt", "w", stdout);
	scanf("%d",&n);
	int k=0;
	while(k++<n)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		int num=X+1;
		dp[0]=C/2;
		bool flag=0;
		double ans=X/2;
		for(int i=1;i<=num;i++)
		{
			dp[!flag]=dp[flag]+C/(2+i*F);
			flag=!flag;
				ans=min(dp[flag]+X/(2+(i+1)*F),ans);
		}
		printf("Case #%d: %.7f\n",k,ans);
	}
  return 0;
}