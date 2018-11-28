#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int numberOfTestCases;
	cin >> numberOfTestCases;
	
	for (int i =0; i <  numberOfTestCases;i++){
		int S1 =0 , S2 =0;
		int numberOfIntervals;
		cin >> numberOfIntervals;
		vector<int> numOfMushrooms (numberOfIntervals);
		int largestRate = 0;
		
		for(int j = 0; j < numberOfIntervals ; j++){
			cin >> numOfMushrooms[j];
			if(j>0){
				int diff = numOfMushrooms[j-1] - numOfMushrooms[j];
				if (diff > largestRate)
					largestRate = diff;
			}	
		}
		
		// first method
		if (numberOfIntervals > 1){
			for(int j =1; j <  numberOfIntervals; j++){
				if (numOfMushrooms[j] < numOfMushrooms[j-1]){
					S1 += (numOfMushrooms[j-1] - numOfMushrooms[j]);
				}
			}
		}
		// second method
		
		if (numberOfIntervals > 1){
			for(int j = 0; j < numberOfIntervals - 1; j++){
				if (numOfMushrooms[j] < largestRate){
					S2 += numOfMushrooms[j];
				}else if(numOfMushrooms[j] >= largestRate){
					S2 += largestRate;
				}
			}
		}
		
		int testCase = i+1;
		cout << "Case #" << testCase << ": " << S1 << " " << S2 << endl;
		
	}
	return 0;
}