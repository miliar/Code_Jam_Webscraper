#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	// your code goes here
	int numCases;
	cin >> numCases;
	for(int i=0; i<numCases; i++){
		int nums[2500];
		int n;
		cin >> n;
		for(int x=0; x<2500; x++){
			nums[x] = 0;
		}
		for(int x=0; x<2*n-1; x++){
			for(int y=0; y<n; y++){
				int temp;
				cin >> temp;
				nums[temp-1]++;
			}
		}
		cout << "Case #" << i+1 << ":";
		for(int x=0; x<2500; x++){
			if((nums[x]%2 != 0))
				cout << " " << x+1;
		}
		cout << "\n";
	}
	return 0;
}