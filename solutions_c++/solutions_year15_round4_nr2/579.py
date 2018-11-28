#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;

int n;
double expv,expt;
double v[105],t[105];
const double delta=0.00001;

double f_v1(double v0){
	double tmp=expv*expt-v0*t[0];
	return tmp/t[1];
}

double time_v0(double v0){
	double v1=f_v1(v0);
	return max(v0/v[0],v1/v[1]);
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("bout1.txt", "w", stdout);
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		scanf("%d%lf%lf",&n,&expv,&expt);
		for(int i=0;i<n;i++){
			scanf("%lf%lf",v+i,t+i);
		}
		printf("Case #%d: ",Case);
		if(n==1){
			if(t[0]!=expt){
				puts("IMPOSSIBLE");
			}else{
				printf("%.9f\n",expv/v[0]);
			}
		}else{
			if(t[1]<t[0]){
				swap(t[1],t[0]);
				swap(v[1],v[0]);
			}
			if(fabs(t[0]-t[1])<1e-6){
				v[0]+=v[1];
				if(fabs(expt-t[1])<1e-6){
					printf("%.9f\n",expv/v[0]);
				}else{
					puts("IMPOSSIBLE");
				}
			}else if(expt>t[1]||expt<t[0]){
				puts("IMPOSSIBLE");
			}else if(fabs(expt-t[1])<1e-6){
				printf("%.9f\n",expv/v[1]);
			}else if(fabs(expt-t[0])<1e-6){
				printf("%.9f\n",expv/v[0]);
			}else{
				double v0=expv*(expt-t[1])/(t[0]-t[1]);
				double v1=expv-v0;
				//printf("%.9f %.9f %.9f %.9f\n",v0,v[0],v1,v[1]);
				printf("%.9f\n",max(v0/v[0],v1/v[1]));
			}
		}
	}
    return 0;
}

