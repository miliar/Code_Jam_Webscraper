#include <bits/stdc++.h>
using namespace std;

long long x,r,c,tt=1,t;

int main()
{
	cin>>t;
	while(tt<=t)
	{
	cin>>x>>r>>c;
	if(x==1)printf("Case #%lld: GABRIEL\n",tt);
	else if(x==2)
    {
        if(r*c % 2==0)printf("Case #%lld: GABRIEL\n",tt);
        else printf("Case #%lld: RICHARD\n",tt);

    }
	else if((r*c)%x!=0)
	{
		printf("Case #%lld: RICHARD\n",tt);

	}
	else if(!((r>x/2)&&(c>x/2)))
	{
		printf("Case #%lld: RICHARD\n",tt);

	}
	else if(!((r>=x)||(c>=x)))
	{
		printf("Case #%lld: RICHARD\n",tt);

	}
	else printf("Case #%lld: GABRIEL\n",tt);
	tt++;
	}
	return 0;
}
