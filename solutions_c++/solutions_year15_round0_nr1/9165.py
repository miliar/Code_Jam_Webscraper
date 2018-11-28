#include <iostream>
using namespace std;

int const MAX_SHY = 1000;

int main(){

	//iterate for numRound
	int round;
	cin >> round;
	for(int i = 0; i < round; i++){
		//get input for every case
		int maxShy;
		string shyA;
		int a[MAX_SHY];
		cin >> maxShy >> shyA;
		for(int j = 0; j <= maxShy; j++){
			a[j] = shyA[j] - '0';
		}

		//now a[] holds the shyness array
		//we now have to check if there are enough people to trigger every level
		int count = 0, add = 0;
		for(int j = 0; j <= maxShy; j++){
			if(count + add < j){
				add += j - count - add;
			}
			count += a[j];
		}

		cout << "Case #" << i+1 << ':' << ' ' << add << endl;
	}

	return 0;
}
