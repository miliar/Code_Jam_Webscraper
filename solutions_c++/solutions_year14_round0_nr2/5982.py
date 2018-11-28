#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main() {
	int N; 
	cin>> N ; 

	for(int T = 1 ; T <= N ; T++) {
		double C, F, X;
		cin>> C >> F >> X ; 

		double sec = 0;
		double per = 2.0;
		double minValue = X / per + sec ;

		while(1)
		{
			double curPer = per + F;
			double curSec = C / per + sec;
			double curValue = X / curPer + curSec; 

			if(curValue <= minValue) {
				per = curPer;
				sec = curSec;
				minValue = curValue;
			}
			else
				break;
		}
		printf("Case #%d: %.7f\n", T, minValue);
		//cout<<"Case #"<<T<<": "<<minValue<<endl;
	}
	return 0 ;
}