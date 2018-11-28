#include <iostream>
#include <cmath>
using namespace std;
int main(){
	int cases;
	cin>>cases;
	double C,F,X;
	double secs,rate;
	double cookies;
	for(int t=1;t<=cases;t++){
		secs=0;
		rate=2;
		cin>>C>>F>>X;
		if(X<=C)
			secs = X/rate;
		else{
			cookies = 0;
			while(cookies!=X){
				secs += C/rate;
				cookies += C;
				if((X-cookies)/rate > X/(rate+F)){
					rate += F;
					cookies -= C;
				}
				else{
					secs += (X-cookies)/rate;
					cookies += (X-cookies);
				}
			}
		}
		printf("Case #%d: %.7lf\n",t,secs);
	}
	return 0;
}