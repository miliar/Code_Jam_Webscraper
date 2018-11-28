#include <cstdio>
const double thereshold=0.00000001;
int main(){
	int T;
	scanf("%d",&T);
	for(int caseNumber=1;caseNumber<=T;++caseNumber){
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double l=0,r=x/2;
		for(;r-l>thereshold;){
			double mid=(l+r)/2;
			double time=0,nexttime,speed=2,total;
			nexttime=c/speed;
			for(;(mid-nexttime)*f>c;){
				time=nexttime;
				speed+=f;
				total=(mid-time)*speed;
				if(total>=x) break;
				nexttime+=c/speed;
			}
			total=(mid-time)*speed;
			if(total>=x) r=mid;
			else l=mid;
		}
		printf("Case #%d: %.7f\n",caseNumber,l);
	}
}

