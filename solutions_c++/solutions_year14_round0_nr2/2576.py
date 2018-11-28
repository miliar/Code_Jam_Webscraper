#include<cstdio>
#include<algorithm>
using namespace std;
// X is rem cookies
inline double go(double C,double F,double X)
{
	double ans=1e20;
	double t=0,r=2.0;
	int iter=1e6;
	while(iter--){
		ans=min(ans,t+X/r);
		t+=C/r;
		r+=F;
		ans=min(ans,t+X/r);
		if(t> ans) break;
	}

	return ans;
}

int main()
{

	int T,tc=1;
	scanf(" %d",&T);
	while(T--) {
	double C,F,X;
	scanf(" %lf %lf %lf",&C,&F,&X);
	printf("Case #%d: %.7f\n",tc++,go(C,F,X));
	}
	return 0;
	
}
