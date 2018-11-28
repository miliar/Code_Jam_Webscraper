#include<iostream>
#include<map>
using namespace std;
int rec1[4][4];
int rec2[4][4];
double dp[100002];
int main()
{
	int n;
	freopen("F://B-large.in","r",stdin);
	freopen("F://out2.txt", "w", stdout);
	scanf("%d",&n);
	int k=0;
	while(k++<n)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		int num=X+1;
		double min=X/2;

		for(int i=0;i<=num;i++)
		{
			if(i==0)dp[0]=C/2;
			else dp[i]=dp[i-1]+C/(2+i*F);
			if(min>dp[i]+X/(2+(i+1)*F))
				min=dp[i]+X/(2+(i+1)*F);
		}
		printf("Case #%d: %.7f\n",k,min);
	}
  return 0;
}