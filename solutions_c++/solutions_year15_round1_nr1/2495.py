#include<cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int ix=0;ix<T;ix++)
	{
		int n;
		scanf("%d",&n);
		int ms[2000];
		for(int i=0;i<n;i++)
		{
			scanf("%d",&ms[i]);
		}
		int ans1=0, ans2=0,rate = 0;
		for(int i=0;i<n-1;i++)
		{
			if(ms[i+1]<ms[i])
				ans1+=ms[i]-ms[i+1];
			if(ms[i]-ms[i+1]>rate)
				rate = ms[i]-ms[i+1];
		}
		for(int i=0;i<n-1;i++)
		{
			if(ms[i]>rate)
				ans2+=rate;
			else
				ans2+=ms[i];
		}
		printf("Case #%d: %d %d\n",ix+1,ans1,ans2);
	}
	return 0;
}