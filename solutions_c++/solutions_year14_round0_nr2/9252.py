#include<cstdio>
#include<algorithm>
using namespace std;

double cost, f, x;

int caso, C;

void doCase(){
	scanf("%lf%lf%lf", &cost, &f, &x);
	
	double time = 0;
	double ans = x/2;
	double frecuency = 2;
	
	for(int i = 1; cost * i < x; ++i, frecuency += f){
		time += cost / frecuency ;
		ans = min(ans, time + x / (frecuency + f) );
	}

	printf("Case #%d: %.7lf\n",++caso, ans);
}

int main(){
	caso = 0;
	scanf("%d",&C);
	for(int i = 0; i < C; ++i)doCase();
}
