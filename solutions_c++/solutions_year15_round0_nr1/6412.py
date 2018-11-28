#include <iostream>
#include <string>

using namespace std;

int main(void){

	ios::sync_with_stdio(false);

	int T, S;
	int current, allPeople, invited;
	string A;

	cin >> T;

	for(int k=1; k<=T; k++){

		cin >> S >> A;

		allPeople = 0;
		invited = 0;

		for(int i=0; i<(int)A.size(); i++){
			current = A[i]-'0';

			if( current ){
				if( allPeople < i ){
					invited += i - allPeople;
					allPeople += i - allPeople;
				}

				allPeople += current;
			}
		}

		cout << "Case #" << k << ": " << invited << endl;
	}

	return 0;
}
