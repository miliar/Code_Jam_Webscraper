#include <stdio.h>
int T;

int TestCase=0;
void make() {
	double C,F,X;
	double income;

	double totalTime;
	scanf("%lf",&C);
	scanf("%lf",&F);
	scanf("%lf",&X);

	income=2.0; //unearned income;
	totalTime =0;
	while( X/income > ( C/income + X/(income+F))) {
		totalTime += C/income;
		income+=F;
	}
	totalTime+= X/income;


	printf("Case #%d: %.7lf\n",++TestCase,totalTime);
}


int main() {
	scanf("%d",&T);
	for(int i=0;i<T;i++)
		make();
	return 0;
}
