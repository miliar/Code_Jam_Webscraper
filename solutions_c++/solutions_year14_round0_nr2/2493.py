#include <iostream>
using namespace std;

double cal(double C, double F, double X){
	if ( C>=X){
		return X/2;
	}
	double curSpeed = 2;
	double curTime = C/curSpeed;
	while(1){
		double timeNotBuy = (X-C)/curSpeed;
		double timeBuy = X/(curSpeed+F);
		if(timeNotBuy <= timeBuy){
			return curTime + timeNotBuy;
		}
		curSpeed += F;
		curTime += C/curSpeed;
	}

}


int main(){
	double C,F,X;
	int T;
	cin>>T;
	for(int cc = 0;cc<T;++cc){
		cin>>C>>F>>X;
		double res = cal(C,F,X);
		printf("Case #%d: %.7f\n", cc+1, res);
	}
}