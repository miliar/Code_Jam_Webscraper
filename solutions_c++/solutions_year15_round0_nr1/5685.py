#include<stdio.h>
char s[1000006];
long long int a[1000006];
int main()
{
	freopen("abc.txt","r",stdin);
	freopen("test.txt","w",stdout);
	long long int f1,f,n,i,x,ans;
	scanf("%lld",&f);
	for(f1=1;f1<=f;f1++)
	{
		scanf("%lld",&n);
		scanf("%s",s);
		n++;
		for(i=0;i<n;i++)
		{
			a[i]=s[i]-'0';
		}
		x=0;
		ans=0;
		for(i=0;i<n;i++)
		{
			if(x!=0)
			{
				x--;
				x=x+a[i];
			}
			else
			{
				if(a[i]!=0)
				{
					x=a[i]-1;
				}
				else
				{
					ans++;
				}
			}
		}
		printf("Case #%lld: %lld\n",f1,ans);
	}
	return 0;
}
		
