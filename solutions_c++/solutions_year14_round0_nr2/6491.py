#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

int T;
double C,F,X,cps = 2;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case<=T;Case++){
		scanf("%lf%lf%lf",&C,&F,&X);
		cps = 2.0;
		double time = 0.0;
		double Min = X/cps;
		while(time <= Min){
			if(Min >= time + X/cps){
				Min = time + X/cps;
			}
			else{
				break;
			}
			time += C/cps;
			cps += F;
		}
		printf("Case #%d: %.7lf\n",Case,Min);
	}
}
