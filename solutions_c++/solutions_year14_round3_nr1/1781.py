#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <set>
using namespace std;

int T;
long long P,Q;



int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		scanf("%lld/%lld",&P,&Q);
		for(long long a=1;a*a<=Q;a++)
		{
			if( Q%a==0 )
			{
				long long b = Q/a;
				if(P%a==0)
				{
					Q/=a;P/=a;
				}
				if(P%b==0)
				{
					Q/=b;P/=b;
				}
			}
		}
		bool ok = false;
		for(long long a=2,cnt=0;cnt<=40;cnt++)
		{
			if( a==Q )
				ok = true;
			a*=2;
		}
		
		int ret = 0;
		while(Q>P)
		{
			Q/=2;
			ret++;
		}
		
		if(ok)
			printf("Case #%d: %d\n",cas,ret);
		else
			printf("Case #%d: impossible\n",cas);
	}
	return 0;
}
