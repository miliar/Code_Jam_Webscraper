#include <cstdio>

using namespace std;

long double min(long double a,long double b){return a<b?a:b;}
long double x,c,f;
int T;

int main()
{
	scanf("%d",&T);
	for(int run=1;run<=T;++run){
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		long double mintime=300000.0,neededtime=0.0,cookierate=0;
		while(cookierate<x*4){
			if(cookierate==0)cookierate=2;
			if(mintime>x/cookierate+neededtime)
				mintime=x/cookierate+neededtime;
			else
				break;
			neededtime+=c/cookierate;
			cookierate+=f;
		}
		printf("Case #%d: %7.7Lf\n",run,mintime);
	}
	return 0;
}
