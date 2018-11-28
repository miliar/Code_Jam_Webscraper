#include<cstdio>
int main() {
	int z;
	scanf("%d",&z);
	for(int _z=1;_z<=z;_z++) {
		double c,f,x,t=0.0,ans;
		scanf("%lf %lf %lf",&c,&f,&x);
		ans=x/2.0;
		for(double i=0;;i+=1.0) {
			t+=c/(i*f+2.0);
			if(t+x/((i+1.0)*f+2.0)<ans)
				ans=t+x/((i+1.0)*f+2.0);
			if(t>=ans)break;
		}
		printf("Case #%d: %lf\n",_z,ans);
	}
	return 0;
}
