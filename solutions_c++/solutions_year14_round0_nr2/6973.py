#include <cstdio>

using namespace std;


double farmCost, rate, winCost, rateAdd;

double result(){
	double diff = winCost-farmCost;
	double tot=0;
	while(diff*(rate+rateAdd)>winCost*rate){
		tot+=farmCost/rate;
		rate+=rateAdd;
	}
	tot+=winCost/rate;
	return tot;
}

int main(){
	int nbCases;
	scanf("%d", &nbCases);
	for(int iCase=1; iCase<=nbCases; iCase++){
		rate=2.0;
		scanf("%lf%lf%lf", &farmCost, &rateAdd,&winCost);
		printf("Case #%d: %lf\n", iCase, result());
	}
}
