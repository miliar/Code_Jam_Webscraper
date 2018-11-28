#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

const double error = 1e-9;

int compare(double a, double b){
	if( fabs(a-b) < error) return 0;
	else if (a-b < 0.0) return 1;
	else return -1;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("large.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tt=1;tt<=test;tt++){
		double x,c,f;
		double persecond = 2.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		double last = 0;
		while(true){
			if( compare(x/persecond, c/persecond + x/(persecond + f)) == -1){
				last+= c/persecond;
				persecond+=f;
			}else {
				last+= x/persecond;
				break;
			}
		}

		printf("Case #%d: %.7lf\n",tt,last );

	}
	return 0;
}