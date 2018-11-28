#include <cstdio>
#include <cmath>
int dig[10000];
bool palin(int x)
{
	int i=0,num=0;
	while(x)
	{
		dig[num++] = x%10;
		x/=10;
	}
	for(i=0;i<num/2+1;i++)
		if(dig[i] != dig[num-1-i]) return false;
	return true;
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int x,a,b,t,T,count;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		count = 0;
		scanf("%d%d",&a,&b);
		x = (int)sqrt(a);
		while(x*x<a) x++;
		for(;x*x<=b;x++)
		{
			if(palin(x) && palin(x*x))
				count++;
		}
		printf("Case #%d: %d\n",t,count);
	}
}