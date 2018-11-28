#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int t;
double c, f, x;
double wyn, czas, farmy;
int main(){
	scanf("%d", &t);
	for(int z=1; z<=t; z++){
		czas=0.0;
		farmy=2.0;
		wyn=0.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		wyn=(x/2);
		while(wyn>czas+c/farmy+x/(farmy+f)  ){
			wyn=czas+c/farmy+x/(farmy+f);
			czas+=c/farmy;
			farmy+=f;
		}
		printf("Case #%d: %.7lf\n", z, wyn);
	}
	return 0;
}
