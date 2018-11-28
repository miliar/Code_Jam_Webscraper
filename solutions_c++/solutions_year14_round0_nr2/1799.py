#include<cstdio>
#include<cstring>
#include<algorithm>
#define eps (1e-9)
using namespace std;

int test;
double C,F,X;

int sgn(double x){
	if (x>eps) return 1;
	if (x<-eps) return -1;
	return 0;
}
int main(){
	freopen("i.txt","r",stdin);
	scanf("%d",&test);
	for (int testcase=1;test--;testcase++){
		printf("Case #%d: ",testcase);
		scanf("%lf%lf%lf",&C,&F,&X);
		if (sgn(C-X)>=0){
			printf("%.7lf\n",X/2.0);
			continue;
		}
		double ans=X/2.0,tot=0;
		for (int i=1;i<=200000;i++){
			double tmp;
			tot+=C/(2.0+(i-1)*F);
			tmp=tot+X/(2.0+i*F);
			if (sgn(tmp-ans)<=0){
				ans=tmp;
			}
		//	printf("%.7lf\n",tmp);
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}
