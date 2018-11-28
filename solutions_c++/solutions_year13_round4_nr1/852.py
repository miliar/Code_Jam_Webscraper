#include <iostream>

using namespace std;
int stop[200];
int n,m;
int calc(int p)
{
	return (n-p+1+n)*p/2;
}
int work(int st,int ed)
{
	if (st>ed) return 0;
	int min=1e9,index=0;
	for (int i=st;i<=ed;i++)
		if (stop[i]<min) {min=stop[i];index=i;}
	for (int i=st;i<=ed;i++)
		stop[i]-=min;

	int ans = calc(ed-st+1)*min+work(st,index-1)+work(index+1,ed);
	//printf("%d---=%d))%d\n",min,index,ans);
	return ans;
}
int main()
{
	int tt;
	scanf("%d",&tt);
	for (int ri=1;ri<=tt;ri++)
	{

		scanf("%d %d",&n,&m);

		memset(stop,0,sizeof(stop));
		int ori=0,sum=0;
		for (int i=0;i<m;i++)
		{
			int a,b,p;
			scanf("%d %d %d",&a,&b,&p);
			for (int j=a;j<b;j++)
				stop[j]+=p;
			ori+=calc(b-a)*p;
		}
		printf("Case #%d: %d\n",ri,ori-work(1,n-1));


	}
    return 0;
}
