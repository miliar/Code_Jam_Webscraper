#include <cstdio>
#include <algorithm>
using namespace std;
int main(){
	int t;
	int tt=0;
	scanf(" %d",&t);
	while(tt<t){
		tt++;
		double c,f,x;
		scanf(" %lf %lf %lf",&c,&f,&x);
		double rate=2;
		if(x<=c){
			printf("Case #%d: %f\n",tt,(x+0.0)/rate);
			continue;
		}
		double timer=(double)c/rate,eat=0;
		double timex=(double)x/rate;
		//double timec=(double)c/rate;
		rate=rate+f;
		while(true){
			eat=(double)x/rate + timer;
			if(eat<timex)
			timex=eat;
			else
			break;
			timer=timer+((double)c/rate);
			rate=rate+f;
		}
		printf("Case #%d: %.7lf\n",tt,timex);


	}

}