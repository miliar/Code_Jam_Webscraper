/*
 * Nareg Deraveneseian
 */

#include <iostream>
#include <string>
#include <iomanip>
#include <vector>
#include <queue>
#include <list>
#include <cmath>
#include <cstdlib>
#include <sstream>      // stringstream

using namespace std;

// We need this function to define how to sort
// the vector. We will pass this function into the
// third parameter and it will tell it to sort descendingly.
bool wayToSort(int i, int j) { return i > j; }

bool readFile(){
	string line, data;
	int counter = 0;
	int tmp = 0;
	int ioBurstCount =0;
//	int size = 1200;
//	int arr[size];
	int arr;
	int numCases;
	int max;
	int case1=0;
	int minutes = 0;
	int numAttended = 0;
	int div = 2;
	getline(cin, line);
	stringstream inData(line);
	stringstream (line) >> numCases;			// nice value

	while(true){
		getline(cin, line);
		if(cin.eof()){
			cin >> line;
			if(line == "***")
				break;
			return false;
		}
		stringstream (line) >> max;			//
		// reseting arr
//		int arr [max];
		vector<int> arr(max);
//		cout << "max: " <<max<<endl;

		getline(cin, line);
		stringstream inData(line);
		int i = 0;
		while(getline(inData, data, ' ')){
			istringstream (data) >> tmp;
			arr[i] = tmp;
			i++;
		}
		bool split = true;
		int xProfit = 0;
		minutes=0;
		// check to see if it worth to split it
		while(split){
			div = 2;
			sort(arr.begin(), arr.end(), wayToSort);
			if(arr[0] == 9){
				if(max > 1){
					// check for next number
					if(arr[1] <= 3 || arr[1] == 6)
						div = 3;
				} else
					div = 3;
			}

			int profit = arr[0]/div;
			int profit2 = arr[0] - profit;
//			if (arr[1] > arr[0])
//				profit = arr[1];
			if(profit == 0){
				split = false;
				break;
			}
			xProfit = 0;
			for(int j = 1; j < max; j++){
				if(j>=profit){
//					cout << j << " " << profit<<endl;
					split = false;
					break;
				}
				if(profit < arr[j]){
					xProfit++;
				} else
					break; // do split
				if(profit == arr[j] || profit2 == arr[j])
					break;
				if(arr[j] + 1 < arr[0])
					break;
			}
			if(split == true){
				minutes++;
//				cout << "split "<< arr[0] << endl;
				tmp = arr[0]/div;
				arr.push_back(tmp);
				arr[0] = arr[0] - tmp;
				max = arr.size();
			}
		}
		minutes += arr[0];

//		cout << endl;
		cout << "Case #" << case1 + 1 << ": " << minutes <<endl;
		case1++;
	}
	return true;
}



/*
 * Printing Process variables
 * Used for debuging
 */
void printProcess(){
	cout <<"--------------------------" <<endl;
	cout <<"---------------------------" <<endl;
}


int main() {
	if(!readFile()){				// reading the file
//		cout <<"Error in Reading the file. Make sure the file is in proper format."<<endl;
		return 0;
	}

	return 0;
}










