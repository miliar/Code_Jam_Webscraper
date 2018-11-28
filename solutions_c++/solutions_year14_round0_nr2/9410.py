#include <bits/stdc++.h>
using namespace std;

#define s(n)                        scanf("%d",&n)
#define EPS 1e-7
int main(int argc, char const *argv[])
{
	int T;
	s(T);
	for(int i=1;i<=T;++i){
		printf("Case #%d: ",i);
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double rate=2;
		double ans=x/2;
		double prev=c/2;
		rate+=f;
		while(1){
			double t=x/rate;
			if(ans-prev-t>EPS){
				ans=prev+t;
			}
			else{
				break;
			}
			prev=prev+c/rate;
			rate+=f;
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}