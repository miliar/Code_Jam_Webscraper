#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int T,k;
double X,C,F;

double mymin(double x, double y){
	if (x<y) return x;
	else return y;
}

int main(){
	scanf("%d",&T);
	for (int tt=1; tt<=T; tt++){
		printf("Case #%d: ",tt);
		//scanf("%lf%lf%lf",&C,&F,&X);
		cin>>C>>F>>X;
		//cout<<C <<" "<<F<<" "<<X<<endl;
		k = int(X/C-2/F-1)+1;
		if (k<0) k=0;
		
		double ans=0,best=1e12;
		for (int i=0; i<=k+10; i++){
			
			best=mymin(best,ans+X/(2+i*F));
			ans=ans+C/(2+i*F);
		}
		printf("%.7lf\n",best);
	}
}
