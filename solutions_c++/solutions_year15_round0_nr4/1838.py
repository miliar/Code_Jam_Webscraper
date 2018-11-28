#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,tc,c,r,x,tmp,flag;
	scanf("%d",&t);
	tc=1;
	while(tc<=t)
	{
		flag=0;
		scanf("%d%d%d",&x,&r,&c);
		tmp=int(x/2);
		if((r*c)%x==0 && (r*c)>=x)
		{
			if(x==1 || x==2)
				flag=0;
			else if(r<=tmp || c<=tmp)
				flag=1;
		}
		else
			flag=1;
		if(flag==1)
			printf("Case #%d: RICHARD\n",tc);
		else
			printf("Case #%d: GABRIEL\n",tc);
		tc++;
	}
	return 0;
}