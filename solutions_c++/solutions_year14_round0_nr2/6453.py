#include <cstdio>
using namespace std;

int main(){
	int testcases;
	scanf("%d",&testcases);
	for(int testcase = 1; testcase <= testcases; testcase++){
		double c,f,x,r=2,nf,wbf,abf,t=0;
		scanf("%lf%lf%lf",&c,&f,&x);
		wbf = x/r;
		nf = c/r;
		abf = x/(r+f);
		while(wbf>nf+abf){
			r += f;
			t += nf;
			wbf = x/r;
			nf = c/r;
			abf = x/(r+f);
		}
		t += wbf;
		printf("Case #%d: %.7lf\n", testcase, t);
	}
	return 0;
}
