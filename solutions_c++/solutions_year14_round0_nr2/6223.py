#include <iostream>
#include <iomanip>
using namespace std;

double currTime, currMoney, growthRate, C, F, X;

bool buyFarm(){
	double t1 = (X-currMoney+C)/(growthRate+F);
	double t0 = (X-currMoney)/growthRate;
	if (t1<t0)
		return 1;
	else
		return 0;
}

void makeMoney(){
	double timeShift = (double)(C-currMoney)/growthRate;
	currTime = currTime + timeShift;
	currMoney = C;
}


void buy(){
	currMoney = currMoney - C;
	growthRate = growthRate + F;
}


int main(){
	int numCase;
	cin >> numCase;
	for (int testcase=1; testcase<=numCase; testcase++){
		currTime = 0;
		currMoney = 0;
		growthRate = 2;
		cin >> C >> F >> X;
		while(currMoney<X){
			makeMoney();
			//cout << "currMoney: " << currMoney << endl;
			//cout << "currTime: " << currTime << endl;

			if(buyFarm()){
				buy();
			} else {
				currTime = currTime + (X-currMoney)/growthRate;
				cout << setprecision(15)<< "Case #" << testcase << ": " << currTime << endl;
				currMoney = X;
			}	
		}		
	}
	return 0;
}
