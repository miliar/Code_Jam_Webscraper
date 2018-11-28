#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main(){
	int T,caseNum=1;
	cin >> T;
	double minTime;
	while(caseNum<=T){
		double C,F,X,rate=2,time=0;
		cin >> C >> F >> X;
		while(1){
			if(X/rate <= (C/rate+X/(rate+F))){
				time += X/rate;
				break;
			}
			else{
				time += C/rate;
				rate+=F;
			}
		}
		cout <<  "Case #"<<caseNum<<": " << setprecision(7)<<fixed<<time<<endl;
		caseNum++;
	}
	return 0;
}


