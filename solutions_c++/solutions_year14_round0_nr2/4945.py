#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int T;
	double c,f,x,ans,val;
	cin>>T;
	for(int testCase=1;testCase<=T;++testCase){
		cin>>c>>f>>x;
		ans=0;
		val=2;
		while(1){
			if( (x/val) <= (x/(val+f))+(c/val) ){
				ans+=(x/val);
				break;
			}
			ans+=(c/val);
			val+=f;
		}
		printf("Case #%d: %.7lf\n",testCase,ans);
	}	
	return 0;
}