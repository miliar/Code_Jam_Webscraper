#include <bits/stdc++.h>

using namespace std;

int TC,caseNo;
double c,f,x;

int main() {
	scanf("%d",&TC);
	while(TC--) {
		printf("Case #%d: ",++caseNo);
		double ans = 1000000000;
		double tmp = 0;
		double jml = 2;
		scanf("%lf %lf %lf",&c,&f,&x);
		while(tmp < ans) {
			ans = min(ans,tmp+x/jml);
			tmp = tmp+c/jml;
			jml+=f;
		}
		printf("%.7lf\n",ans);
	}
}