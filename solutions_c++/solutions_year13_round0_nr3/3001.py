#include <stdio.h>
#include <string.h>
#include <math.h>
bool pal(int x)
{
	int s[99],i;
	for(i=0;x;i++)
	{
		s[i]=x%10;
		x/=10;
	}
	int j=0;
	i--;
	while(j<i)
	{
		if(s[j]!=s[i])return 0;
		i--;
		j++;
	}
	return 1;
}
bool is(int x)
{
	if(!pal(x))return 0;
	int i=sqrt(x+0.0);
	if(i*i!=x)return 0;
	if(!pal(i))return 0;
	return 1;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int k,i,j,a,b;
	scanf("%d",&cas);
	for(k=1;k<=cas;k++)
	{
		printf("Case #%d: ",k);
		int sum=0;
		scanf("%d%d",&a,&b);
		for(i=a;i<=b;i++)
			if(is(i))
			{
				sum++;
				//printf("%d\n",i);
			}
		printf("%d\n",sum);
	}
	return 0;
}