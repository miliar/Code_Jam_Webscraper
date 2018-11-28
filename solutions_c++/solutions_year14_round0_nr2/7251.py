#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main()
{
	int t;
	double C;
	double F;
	double X;
	double c[501] = {0};
	double sum[501] = {0};
	scanf("%d",&t);
	int ii = 1;
	while(t--) {
		scanf("%lf%lf%lf",&C,&F,&X);
		double j = 2;
		double ans = 0;
		double temp = X/2;
		for(int i = 0 ; i < 501; i++) {
			c[i] = 0;
			sum[i] = 0;
		}
		c[0] = C/2;
		if(c[0] == X) {
			printf("Case #%d: %0.7lf\n",ii,c[0]);
			ii++;
		}else if(C  < 2.00000000) {
			while(1){
				if((X/j) < (C/j + X/(F+j))) {
					ans+= X/j;
					printf("Case #%d: %0.7lf\n",ii,ans);
					ii++;
					break;
				}else{
					ans+= C/j;
					j = F + j;
				}
			}
		}
		else{
			sum[0] = 0;
			temp = X/2;
			c[0] = 0;
			for(int i = 1; i < 2000; i++) {
				c[i] = c[i-1] + C/j;
				sum[i] = c[i] + X/(F+j);
				j = j + F;
				//cout << sum[i] << endl;
				if(sum[i] > temp){
					printf("Case #%d: %0.7lf\n",ii,temp);
					ii++;
					break;
				}
				temp = sum[i];
			}	
		}			

	}
	return 0;
}

