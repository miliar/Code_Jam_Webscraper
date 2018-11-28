#include<stdio.h>
#include<math.h>
bool pal(int n)
{
	int t=n,rev=0;
	while(n!=0)
	{
		rev=rev*10+(n%10);
		n/=10;
	}
	if(rev==t)
		return true;
	return false;	
}
int main()
{
	int t,a,b,c,n;
	//freopen("input.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d%d",&a,&b);
		c=0;
		for(int x=a;x<=b;x++)
		{
			n=sqrt(x);
			if(((n*n)==x) && pal(x) && pal(n))
				c++;
		}
		printf("Case #%d: %d\n",i,c);
	}
}
