#include <iostream>
using namespace std;


int main() {
	// your code goes here
	int numCases;
	cin >> numCases;
	for(int i=0; i<numCases; i++){
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << i+1 << ": ";
		for(int i = 1; i < k; i++)
			cout << i << " ";
		cout << k << "\n";
	}
	return 0;
}