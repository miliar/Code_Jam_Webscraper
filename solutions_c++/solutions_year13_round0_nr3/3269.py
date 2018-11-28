#include <cstdio>
#include <cstring>
#include <cmath>
bool judge(int a)
{
	int ans=0,t=a;
	while(a>0)
	{
		ans=ans*10+a%10;
		a/=10;
	}
	if(ans==t)
		return true;
	return false;
}
int main()
{
	int d=1,i,t,a,b,sa,sb,c;
	scanf("%d",&t);
	while(t--)
	{
		c=0;
		scanf("%d %d",&a,&b);
		sa=(int)sqrt((double)a),sb=(int)sqrt((double)b);
		for(i=sa;i<=sb+1;i++)
		{
			if(judge(i)&&judge(i*i)&&(i*i>=a)&&(i*i<=b))
				c++;
		}
		printf("Case #%d: ",d++);
		printf("%d\n",c);
	}
	return 0;
}
