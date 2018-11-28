#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(){
	int numCases;
	int currentCase = 0;
	cin >> numCases;
	cout << setiosflags(ios::fixed) << setprecision(7);
	while(currentCase++ < numCases){
		//int numFarms;
		long double farmPrice, goal, rate, farmRate;//, numCookies;
		cin >> farmPrice >> farmRate >> goal;
		rate = 2;
		long double timer = 0;
		//every time while conditional evaluated numCookies should be 0
		//while time to goal < time to goal if farm is bought, buy farm
		while((goal / rate) > ((farmPrice/rate) + (goal / (rate + farmRate)))){
			timer += farmPrice/rate;
			rate += farmRate;
		}
		timer += goal/rate;
		cout << "Case #" << currentCase << ": " << timer << "\n";
	}


	return 0;
}