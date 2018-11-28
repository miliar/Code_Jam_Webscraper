#include <iostream>

using namespace std;

int main(){
	int testCases;
	int maxShyness;
	string shyness;
	int totalStanding, friendsNeeded;

	cin >> testCases;
	for(int j = 0; j < testCases; j++){
		cin >> maxShyness >> shyness;
		totalStanding = 0; friendsNeeded = 0;
		for(int i = 0; i <= maxShyness; i++){
			if (shyness[i] != '0' &&  totalStanding < i){
				friendsNeeded += i - totalStanding;
				totalStanding = i;
			}
			totalStanding += shyness[i] - '0';
		}
		cout << "Case #" << j + 1 << ": " << friendsNeeded << endl;
	}
	return 0;
}