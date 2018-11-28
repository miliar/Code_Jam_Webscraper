#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
//int max(int x,int y){ return x>=y?x:y; }
//int min(int x,int y){ return x<=y?x:y; }
int main()
{
int N;
scanf("%d",&N);
for(int T=1;T<=N;T++)
{
	double c,f,x;
	scanf("%lf%lf%lf",&c,&f,&x);
	int k=max(0,(int)ceil(x/c-1.-2./f));
	double o=x/(2.+k*f);
	for(int a=0;a<k;a++) o+=c/(2.+a*f);
	printf("Case #%d: ",T);
	printf("%.7lf\n",o);
}
	return 0;
}
