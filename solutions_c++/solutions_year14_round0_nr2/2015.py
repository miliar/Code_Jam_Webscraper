#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int k=0;k<t;k++){
		double base=0,mnum;
		double C,F,X,S=2;
		scanf("%lf%lf%lf",&C,&F,&X);
		mnum=X/S;
		while(1){
			if(base+X/S<mnum)mnum=base+X/S;
			if(base+C/S+X/(S+F)<=mnum){
				base+=C/S;
				S+=F;
				mnum=base+X/S;
			}else break;
		}
		printf("Case #%d: %.7lf\n",k+1,mnum);
	}
	return 0;
}
