#include <stdio.h>
main()
{
	freopen( "D-small-attempt2.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int t,rsv,lol,x,r,c;
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld%lld%lld",&x,&r,&c);
		if((r*c)%x!=0)rsv=0;
		else if(x>c&&x>r)rsv=0;
		else
		{
			if(x>2&&x%2==0&&(x/2>=r||x/2>=c))
			rsv=0;
			else
			{
				if(x%2==1)x++;
				x=x/2;
				if(x>r||x>c)rsv=0;
				else rsv=1;
			} 
			
		}
		if(rsv==0)
		printf("Case #%lld: RICHARD\n",lol);
		else
		printf("Case #%lld: GABRIEL\n",lol);
	}
}
		
