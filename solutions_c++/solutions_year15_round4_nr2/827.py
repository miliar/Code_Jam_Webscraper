#include <bits/stdc++.h>

using namespace std;

int n,m;
double v,x;
double r[110],c[110];
const double eps =1e-8;

int main(){
	int T;
	scanf("%d",&T);
	for (int ti=1;ti<=T;ti++){
		printf("Case #%d: ",ti);
		scanf("%d%lf%lf",&n,&v,&x);
		double mc=0;
		for (int i=0;i<n;i++) {
			scanf("%lf%lf",&r[i],&c[i]);
			if (c[i]-mc>eps) mc=c[i];
		}
		double minc=mc;
		for (int i=0;i<n;i++){
			if (c[i]-minc<-eps) minc=c[i];
		}
		
		if (mc-x<-eps || x-minc<-eps){
			/*
			if (ti==59){
				cout << v<<" "<<x<<endl;
				for (int i=0;i<n;i++) cout << r[i]<<" "<<c[i]<<endl;
			}
			*/
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		//cout << v<<" "<<r[0]<<endl;
		if (n==1){
			if (fabs(x-c[0])>eps) printf("IMPOSSIBLE\n");
				else printf("%.10f\n",v*1.0/r[0]);
			continue;
		}
		double t=c[0]-c[1];
		//cout << t<<endl;
		if (fabs(t)<eps){
			if (fabs(c[0]-x)>eps) printf("IMPOSSIBLE\n");
				else{
					double ans = v*1.0/(r[0]+r[1]);
					printf("%.10f\n",ans);
				}
		}else{
				double v1 = v*(x-c[1])/t;
				//cout << v1<<endl;
				if (v1<-eps) printf("IMPOSSIBLE\n");
					else {
						double t1=v1/r[0];
						double t2=(v-v1)/r[1];
						if (t2<-eps) printf("IMPOSSIBLE\n");
							else {
							double ans = t1;
							if (t1-t2<-eps) ans=t2;
							printf("%.10f\n",ans);
							}
					}
			}
	}
	return 0;
}

