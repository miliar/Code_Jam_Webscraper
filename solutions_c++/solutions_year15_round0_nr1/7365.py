#include <iostream>
#include <fstream>

using namespace std;

int main(){

	ifstream in("standing_ovation.in");
	ofstream out("standing_ovation.out");

	int cases;
	in >> cases;

	for (int i = 1; i <= cases; i++) {

		int maximum_shyness;
		in >> maximum_shyness;
		string S; //there are S_k people with k shyness level
		in >> S;

		int min_changes = 0, stood_up = 0;
		
		for (int j = 0; j <= maximum_shyness; j++) {

			int shy_people_j = S[j] - '0', need_to_stand_up = 0;
			if (shy_people_j != 0 && stood_up < j) {

				int need_to_stand_up = j - stood_up; //amount of people to break shyness
				min_changes += need_to_stand_up; //add the previous value to the min. amount of changes
				stood_up += need_to_stand_up; //also keep the record of people already standing up

			}
			stood_up += shy_people_j;

		}

		out << "Case #" << i << ": " << min_changes << endl;

	}

	return 0;
}