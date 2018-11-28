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
	int numFriends = 0;
	int numAttended = 0;
	getline(cin, line);
	stringstream inData(line);
	stringstream (line) >> numCases;			// nice value
//	cout << "Number of case: " <<numCases <<endl;

	while(true){
		getline(cin, line);
		if(cin.eof()){
			cin >> line;
			if(line == "***")
				break;
			return false;
		}
		stringstream (line) >> max;			// nice value
		// reseting arr
//		for (int i = 0; i < size; i++){
//			arr[i] = 0;
//		}
		int arr [max];
		stringstream inData(line);
		int i = 0;
		while(getline(inData, data, ' ')){
			if(i!=0){
				//				cout << data;
				// check the thing
				for(int j = 0; j <= max ;j++){
					int k = data[j] - '0';
					arr[j]=k;
				}
				// finding max number
				for(int j = 0; j <= max; j++){
					if(numAttended >= j)
						numAttended += arr[j];
					else if(arr[j] > 0){
						if(j > numAttended){
							int k = j - numAttended;
							numFriends  += k;
							numAttended += k;
							numAttended += arr[j];
						}
					}
				}
				// out put
				cout << "Case #" << case1 + 1 << ": " << numFriends <<endl;
				numFriends=0;
				numAttended = 0;
				case1++;
			}
			i++;
		}
		counter++;
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










