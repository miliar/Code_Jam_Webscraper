#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
double c,f,x;
void solve(int test){
	printf("Case #%d: ", test+1);
	scanf("%lf %lf %lf",&c,&f,&x);
	double res = x/2.0;
	double temp = x/2.0;
	for(int i=1; i<1000001; i++){
		temp -= x/( (i-1)*f+2 );
		temp += c/ ( (i-1)*f + 2);
		temp += x/(i*f+2);
		res = min(res,temp);
	}
	printf("%.7lf\n",res);
}
int ntest;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);		
	for(int t=0; t<ntest; t++){
		
		solve(t);
	}
	return 0;
}
