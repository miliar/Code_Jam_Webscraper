#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	float T;
	float C;
	float F;
	float X;
	float timeShortest = 0.0000000;
	float timeToComplete = 0.0000000;
	float timeToBuild = 0.0000000;
	float timeTotal = 0.0000000;
	int factories = 0.0000000;
	float rate = 2.0000000;
	
	cout << "Beginning..." << endl;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		timeShortest = 0.0000000;
		timeToComplete = 0.0000000;
		timeToBuild = 0.0000000;
		timeTotal = 0.0000000;
		rate = 2.0000000;
		factories = 0.0000000;
		cout << "Case #" << i << ": ";
		cin >> C >> F >> X;
		timeShortest = X / rate;
		//cout << "Time Without Factories: " << timeShortest << endl;
		while(1) {
			factories++;
			//cout << "With " << factories << " factories: " << endl;
			timeToBuild += C / rate;
			//cout << "It will take " << timeToBuild << " seconds to build." << endl;
			rate += F;
			//cout << "The rate will be " << rate << endl;
			timeToComplete = X / rate;
			//cout << "At this rate, it will take " << timeToComplete << " seconds to reach the goal." << endl;
			timeTotal = timeToBuild + timeToComplete;
			//cout << "Finally, the time to build these factories and the time to get the cookies total will be " << timeTotal << " seconds." << endl;
			if(timeTotal < timeShortest) {
				timeShortest = timeTotal;
			}
			else if(timeTotal > timeShortest) {
				cout << fixed;
				cout << setprecision(7) << timeShortest << endl;
				break;
			}
		}
	}
	return 0;
}