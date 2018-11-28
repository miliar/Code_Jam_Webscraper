#include<cstdio>
void solve(int t) {
	double a,b,c;
	scanf("%lf%lf%lf",&a,&b,&c);
	double in=2;
	double sum=0;
	while(1) {
		double x=c/in;
		double y=a/in+c/(in+b);
		if(x<=y) {
			sum+=x;
			break;
		} else {
			sum+=a/in;
			in+=b;
		}
	}
	printf("Case #%d: %.7lf\n",t,sum);
}
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) solve(t+1);
	return 0;
}