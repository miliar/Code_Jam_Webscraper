#include <iostream>
#include <iomanip>
#include <math.h> 
using namespace std;


int main(){
	int numberOfTestCases;
	double c;
	double f;
	double x;
	cin >> numberOfTestCases;
	int caseNumber = 0;
	while(numberOfTestCases--){				
		caseNumber++;		
		cin >> c >> f >> x;
		double timeToBuyFarm = c/2;
		double timeToWin = x/2;
		bool isWorthBuying = true;
		
		double producing = 2;
		double lastCost = x/producing;		
		
		for(int i = 0; i < floor(x/c)+1; i++){
			double costWithBuyingIFarms = 0;
			producing = 2;
			for(int j = 0; j < i; j++){							
				costWithBuyingIFarms = costWithBuyingIFarms + c/producing;
				producing = producing + f;
			}
			costWithBuyingIFarms = costWithBuyingIFarms + x/producing;
		
			if(costWithBuyingIFarms < lastCost){				
				lastCost = costWithBuyingIFarms;
				if(caseNumber == 100){
					//cout << "case 100 cost " << lastCost << " with number of farms being  " << i << "\n";
				}
			}
		}
		cout << setprecision(7) << fixed;
		cout << "Case #" << caseNumber << ": " << lastCost << "\n"; 
	}
	return 0;
}