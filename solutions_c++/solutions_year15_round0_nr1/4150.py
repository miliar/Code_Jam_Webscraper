#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv){
	int iter = 0, T, friends, maxShyness, shy, numPeople, soFar;
	char buf;
	string inp;
	cin >> T;

	while (iter++ != T){
		cin >> maxShyness;

		cin.ignore(1);
		cin.get(buf);
		soFar = buf - '0';

		friends = 0; // =(

		for (shy = 1; shy <= maxShyness; ++shy){
			cin.get(buf);
			numPeople = buf - '0';

			if (soFar < shy){
				friends += shy - soFar;
				soFar = shy;
			}

			soFar += numPeople;
		}

		cout << "Case #" << iter << ": " << friends << endl;
	}

	return 0;
}