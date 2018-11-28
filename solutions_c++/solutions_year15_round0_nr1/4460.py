#include <iostream>
#include <string>

using namespace std;

int main () {
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; ++i) {
		int maxShy;
		cin >> maxShy;
		string inputArray;
		cin >> inputArray;
		int added = 0;
		int total = 0;
		for (size_t j=0; j<inputArray.length(); ++j) {
			int avail = static_cast<int>(inputArray[j]) - static_cast<int>('0');
			if (avail == 0) {
				continue;
			}
			if (j <= total) {
				total += avail;			
			} else {
				added += (j-total);
				total += (j-total);
				total += avail;
				//cout << added;
			}		
		}
		cout << "Case #" << (i+1) << ": " << added << endl; 
	}
}
