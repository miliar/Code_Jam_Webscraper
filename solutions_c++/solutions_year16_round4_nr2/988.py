#include <cstdio>
#include <algorithm>

using namespace std;

#define MX 209

int n,k;
double p[MX];

double get_dp(int i, int k_left, double* needed_p){
/*	for(int j=0;j<i;j++){ printf("  "); }
	printf("dp(%dth, %d left, [",i,k_left);
	for(int j=0;j<=k;j++){
		printf("%lf,",needed_p[j]);
	}
	printf("])\n");*/
	if(i==n){
		if(k_left!=0){ return 0; }
		return needed_p[0];
	}
	double prob1; // probability of success if skipped
	prob1=get_dp(i+1, k_left, needed_p);
	if(k_left==0){
		return prob1;
	}
	double prob2; // probability of success if taken
	double needed_1[MX]; // If votes "Yes"
	double needed_2[MX]; // Otherwise
	double needed_new[MX]; // Sum

	for(int j=0;j<k;j++){
		needed_1[j]=needed_p[j+1] * p[i];
	}
	for(int j=0;j<=k;j++){
		needed_2[j]=needed_p[j] * (1-p[i]);

		needed_new[j]=needed_1[j]+needed_2[j];
	}

	prob2=get_dp(i+1, k_left-1, needed_new);

	return max(prob1, prob2);
}

int main(){
	int t;
	scanf("%d",&t);
	for(int tc=0;tc<t;tc++){
		scanf("%d %d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lf",&p[i]);
		}
		double np[MX];
		for(int i=0;i<MX;i++){
			np[i]=0;
		}
		np[k/2]=1;
		printf("Case #%d: %.9lf\n", tc+1, get_dp(0, k, np));
	}
}
