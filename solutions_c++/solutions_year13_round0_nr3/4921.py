#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int hw(int x)
{
	int tt[10],num=0,i,j;
	while(x)
	{
		tt[num++]=x%10;
		x/=10;
	}
	int flag=1;
	for(i=0,j=num-1;i<j;i++,j--)
		if(tt[i]!=tt[j])
		{
			flag=0;
			break;
		}
	return flag;
}
int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);
	int t,a,b,i,cas=0;
	scanf("%d",&t);
	while(t--)
	{
		int cnt=0;
		scanf("%d%d",&a,&b);
		for(i=a;i<=b;i++)
		{
			if(hw(i))
			{
				int tmp=sqrt(i);
				if(tmp*tmp==i&&hw(tmp))
					cnt++;
			}
		}
		printf("Case #%d: ",++cas);
		printf("%d\n",cnt);
	}
	return 0;
}