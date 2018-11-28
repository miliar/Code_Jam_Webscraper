#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main(){
	int cases;
	double c,f,x;
	freopen("B-large.in","r",stdin);
	freopen("BLout.out","w",stdout);
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%lf%lf%lf",&c,&f,&x);
		double a=2;
		double ans=0;
		if (c>=x){
			printf("Case #%d: %.7lf\n",cas,x/a);
		}
		else {				
			while ((x-c)/a>x/(a+f)){
				ans=ans+c/a;
				a=a+f;
			}
			ans=ans+x/a;
			printf("Case #%d: %.7lf\n",cas,ans);	
		}
	}
	return 0;
}
