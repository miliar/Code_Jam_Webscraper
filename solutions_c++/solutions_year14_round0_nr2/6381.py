#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	double productionRate;
	int testCount;
	int testCase = 1;
	double C, F, X;
	int farms;
	cin >> testCount;
	double previousGoalCost;
	double previousFarmCost;
	double farmCost;
	double goalCost;
	while (testCase <= testCount){
		farms = 0;
		cin >> C >> F >> X;

		productionRate = 2.0;
		previousFarmCost = 0;
		previousGoalCost = X / productionRate;
		while(1){
			++farms;
			farmCost = previousFarmCost + C / productionRate;
			productionRate += F;
			goalCost = X / productionRate;
			if (previousFarmCost+previousGoalCost <= farmCost+goalCost){
				break;
			}
			previousFarmCost = farmCost;
			previousGoalCost = goalCost;
		}

		cout << "Case #" << testCase << ": " << std::setprecision(7) << std::fixed << previousFarmCost + previousGoalCost << endl;
		++testCase;
	}
	return 1;
}