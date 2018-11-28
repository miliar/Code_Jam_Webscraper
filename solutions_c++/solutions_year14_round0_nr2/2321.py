#include <iostream>
#include <stdio.h>
using namespace std;
double greedy(double c,double speed,double extra,double target){
	double n=0;	
	double t=0;
	// cout<<"..............."<<endl;
	while(true){	
		if(n<c){
			double delta=(c-n)/speed;
			n+=delta*speed;
			t+=delta;
			// cout<<t<<":"<<n<<endl;
		}
		while(n>=c) {
			double t1=(double)(target-n)/speed;
			double t2=(double)c/extra;
			if(t1>t2) {
				// cout<<t<<",speed:"<<speed<<" to "<<speed+extra<<" n:"<<n<<endl;
				speed+=extra;n-=c;
			}
			else {
				t+=t1;
				n+=t1*speed;
				return t;
			}
		}
	}
}
int main(){
	int cases;cin>>cases;
	for(int caseI=1;caseI<=cases;caseI++){
		double c,extra,target;
		cin>>c>>extra>>target;
		// cout<<endl<<c<<":"<<extra<<":"<<target<<endl;
		printf("Case #%d: %.7f\n",caseI,greedy(c,2.0,extra,target));//<<endl;
	}
	return 0;
}

