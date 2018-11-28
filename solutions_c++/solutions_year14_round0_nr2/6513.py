//Code Jam Problem B 12/Apr/2014
#include <iostream>

using namespace std;
int main() {
	int numTestCases;
	double cookieRate, timeMinToComplete, tempTime1, tempTime2;
	double C, F, X;
	//Getting Input
	cin>>numTestCases;
	cout.setf( std::ios::fixed, std:: ios::floatfield );
	cout.precision(7);
	for(int i = 1; i <= numTestCases; i++){
		cin>>C;
		cin>>F;
		cin>>X;		
		cookieRate = 2.0;//Initial Cookie rate
		timeMinToComplete = 0.0;//Minimum time in which we have X cookies
		//Loop through until we get the minimum Time for X cookies
		while(1) {
			tempTime1 = timeMinToComplete + (X / cookieRate); //Holds the time which will take if we gather X cookies at the current rate
			tempTime2 = timeMinToComplete + (C / cookieRate); //Holds the time which will take to build the farm
			if(tempTime1 <= (tempTime2 + (X / (cookieRate + F)))) {
				timeMinToComplete = tempTime1;
				break;
			}
			else {
				timeMinToComplete = tempTime2;
				cookieRate = cookieRate + F;
			}
		}
		cout<<"Case #"<<i<<": "<<timeMinToComplete<<"\n";
	}
	
	
	return 0;
}
