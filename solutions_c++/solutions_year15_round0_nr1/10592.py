#include <iostream>
#include <stdio.h>
int main()
{
	int t,i,n,z=1,val,ans,b[1005];
	char a[1005];
	scanf("%d",&t);
	while(z<=t)
	{
		scanf("%d%s",&n,a);
		for(i=0;i<=n;i++)
			b[i]=a[i]-'0';
		ans=0;
		val=b[0];
		for(i=1;i<=n;i++)
		{
			if(!b[i])
				continue;
			if(val<i)
				ans+=i-val,val+=ans;
			val+=b[i];
		}
		printf("Case #%d: %d\n",z,ans);
	z++;}

return 0;}