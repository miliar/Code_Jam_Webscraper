#include <iostream>
#include <cstdio>
using namespace std;
#define sd(x) scanf("%d",&x)
int main() {
	int t,test = 0;
	sd(t);
	while(t--) {
		long double ans = 0.0;
		test++;
		long double buyfarm=0.0;
		long double buyx=0.0;
		long double c,f,x;
		long double cnum=2.0;
		int notdone=1;
		cin>>c>>f>>x;
		if( x < c) {
		ans=x/2.0;
		printf("Case #%d: %.7Lf\n",test,ans);
		} else {
			while(notdone){
				buyfarm=c/cnum + x/(cnum+f);
				buyx=x/cnum;
				if(buyfarm<buyx)
				{
					ans=ans+(c/cnum);
					cnum=cnum+f;
				}
				else
				{
					ans=ans+buyx;
				printf("Case #%d: %.7Lf\n",test,ans);
					notdone=0;
				}
			}
		}
	}
	 return 0;
}

