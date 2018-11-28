#include <cstdio>
#include <cmath>

using namespace std;

long cnt,ct=0,t,i,a,b;

int main () {
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%ld",&t);
	
	while(t--)
	{
		scanf("%ld%ld",&a,&b);
		cnt=0;
		for(i=a;i<=b;i++){
			
			long cx=i,rv=0;
			while(cx)
			{
				rv=rv*10+cx%10;
				cx/=10;
			}
			if(i==rv)
			{
				long cx=(long)sqrt((double)i),rv2=0;
				while(cx)
				{
					rv2=rv2*10+cx%10;
					cx/=10;
				}
				if((long)sqrt((double)i)*sqrt(i)==rv2*rv2 && rv2==sqrt((double)i))
					cnt++;
			}
		}
		printf("Case #%ld: %ld",++ct, cnt);
		printf("\n");
	}
	
	return 0;
}
