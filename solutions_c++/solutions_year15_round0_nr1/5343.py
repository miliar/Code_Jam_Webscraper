#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++){
		
		int lim;
		cin >> lim;
		string shyness;
		cin >> shyness;
		int counter = shyness[0] - '0';
		int numGuests = 0;
		for(int j = 1; j < shyness.length(); j++){
			//cout << counter << endl;
			if(counter < j){
				numGuests++;
				counter++;
			}
			counter+=shyness[j] - '0';
		}
		cout << "Case #" << i << ": ";
		cout << numGuests << endl;
	}
	return 0;
}