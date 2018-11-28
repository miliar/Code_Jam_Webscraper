#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

double time_to_reach_rate_r(double r,double f,double c){
	double time=0,rate=2;
	while(rate<r){
		time += c/rate;
		rate+=f;
	}
	return time;
}

int main(){
	int T,caseNum=1;
	cin >> T;
	double minTime;
	while(caseNum<=T){
		double C,F,X,totalTime=0,rate=2;
		cin >> C >> F >> X;
		minTime = X/rate;
		while(1){
			rate+=F;
			totalTime = time_to_reach_rate_r(rate,F,C) + X/rate;
			if(minTime>totalTime)
				minTime=totalTime;
			if(minTime < time_to_reach_rate_r(rate,F,C))
				break;
		}
		cout <<  "Case #"<<caseNum<<": " << setprecision(7)<<fixed<<minTime<<endl;
		caseNum++;
	}
	return 0;
}


