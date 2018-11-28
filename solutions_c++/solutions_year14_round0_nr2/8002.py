#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	cout.precision(7);
	
	for(int i = 0; i < n; ++i){
		double C,F,X;
		cin >> C >> F >> X;
		
		double prevCost = X/2;
		double cost = 0;
		double currentCost = 0;

		int count = 0;
		//cout << "X/2 = " << X/2 << endl;
		while(true){
			cost += C / (2 + F*count);
			//cout << "Farm Cost = " << cost;
			currentCost = cost + X/(2 + F*(count+1));
			//cout << " Total Cost = " << currentCost << endl;
				
			if((currentCost > X/2) || (currentCost > prevCost))
				break;
			prevCost = currentCost;
			++count;
		}
		
		
		cout << "Case #" << i+1 << ": " << prevCost << std::fixed << endl;
	}
	return 0;
}