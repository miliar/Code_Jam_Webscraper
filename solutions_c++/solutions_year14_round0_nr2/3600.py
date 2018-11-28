#include <cstdio>

using namespace std;

const long eps=1e-6;

double c,f,x,cps=2,total=0;
long tc;

void buynewfarm (void)
{
	cps+=f;
	//cookies-=c;
}

int main () {
	
	freopen("cookie.in","r",stdin);
	freopen("cookie.out","w",stdout);
	
	scanf("%ld",&tc);
	long k=0;
	while(tc--)
	{
		k++;
		scanf("%lf%lf%lf",&c,&f,&x);
		total=0;cps=2;
		while(1)
		{
			if((x-c)/cps-x/(cps+f)>eps){
				total=total+c/cps;
				buynewfarm();
			}
			else{
				total+=x/cps;
				break;
			}
		}
		printf("Case #%ld: %.7lf\n",k,total);
	}
	return 0;
}
