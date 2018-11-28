#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		double C,F,X;
		cin>>C>>F>>X;
		int loop=0;
		while(1){
			double term1=X/(2.0+loop*F);
			double term2=X/(2.0+(loop+1)*F);
			double term3=C/(2.0+loop*F);
			/*if(i==1) cerr<<term1<<' '<<term2<<' '<<term3<<endl;
			if(i==1) cerr<<term1-term2-term3<<endl;*/
			if(term1<=term2+term3){
				break;
			}
			loop++;
		}
		double ans=X/(2+loop*F);
		for(int j=0;j<loop;j++){
			ans+=C/(2+j*F);
		}
		//if(i==1) cerr<<loop<<endl;
		printf("Case #%d: %f\n",i+1,ans);
	}
	return 0;
}