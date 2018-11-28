#include<iostream>
#include<limits>

using namespace std;

//using global variables, no no.
double farmCost, rateIncrease, goal;

/**
 * Calculates the rate of cookies with n farms
 * @param n the number of farms
 */
double rateWithNFarms(int n){
	if (n < 1)
		return 2;
	else
		return 2 + (n * rateIncrease);
}

/**
 * Calculate the amount of time it takes to get N farms
 * Uses the time it took to get N minus 1 farms and adds to 
 * the amount of time it takes to get N farms when already
 * owning N Minus 1 farms.
 * @param numFars the number of farms trying to hit
 * @param timeToNm1Farms time to N Minus 1 farms
 */
double timeToNFarms(int n, double timeToNM1Farms){
	if (n < 1)
		return 0;
	else
		return timeToNM1Farms + ((farmCost)/rateWithNFarms(n-1));
}

/**
 * Processes input to solve and produce results to stdout
 * @param caseNumber the number to output
 */
void processCase(int caseNumber){
	// updating the global variables for this run
	cin >> farmCost >> rateIncrease >> goal;

	double previousTime;
	double currentTime = numeric_limits<double>::max();
	double timeToFarmsM1 = 0;

	int farms = 0;
	do {
		previousTime = currentTime;
		timeToFarmsM1 = timeToNFarms(farms, timeToFarmsM1);
		currentTime = goal/rateWithNFarms(farms) + timeToFarmsM1;
		farms++;
	} while (currentTime < previousTime);

	// previous time was less than current time, previous time is min

	//output
	cout << "Case #" << caseNumber << ": ";
	cout << previousTime;
	cout << endl;
}

int main(void){
	int numCasesPp;
	cin >> numCasesPp;
	numCasesPp++;
	// setting precision to the recommended value
	cout.precision(7);
	cout.setf(ios::fixed, ios::floatfield);
	for (int i = 1; i < numCasesPp; i++){
		processCase(i);
	}
	return 0;
}
