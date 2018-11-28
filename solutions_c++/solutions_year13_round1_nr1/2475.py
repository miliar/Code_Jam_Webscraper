#include <cstdio>
#include <cmath>

using namespace std;

const double PI = 4.0*atan(1.0);

long tC,ct,Black;
double r,t;

int main () {
	
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	
	scanf("%ld",&tC);
	
	while(tC--)
	{
		ct++;Black=0;
		scanf("%lf%lf",&r,&t);
		//r=r+1;
		do{
			t=t-2*r-1;
			Black++;
			r+=2;
		}while(t>=0);
		if(t>=0)
			printf("Case #%ld: %ld\n",ct,Black);
		else
			printf("Case #%ld: %ld\n",ct,Black-1);
	}
	
	return 0;
}

//Bye!!