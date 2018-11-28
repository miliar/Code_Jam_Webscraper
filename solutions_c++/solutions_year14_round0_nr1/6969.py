#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[]){
	
	
	ifstream input;
	ofstream output;

	input.open("./input.txt");
	output.open("./ouput.txt");

	int No_Cases,temp;
	input >> No_Cases;

	for (int f = 0; f < No_Cases; ++f){
		int cards1[4], cards2[4], answera, answerb;

		input >> answera;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++){
				if (answera-1 == x)
					input >> cards1[y]; // row we want
				else
					input >> temp; // go to next
			}

		input >> answerb;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++){
				if (answerb-1 == x)
					input >> cards2[y];
				else
					input >> temp;
			}

		bool got_one = false;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (cards1[i] == cards2[j]){
					if (got_one){
						output << "Case #" << f + 1 << ": Bad magician!" << endl;
						goto Partial_Break;
					}
					got_one = true;
					temp = cards1[i];
				}
		if (!got_one)
			output << "Case #" << f + 1 << ": Volunteer cheated!" << endl;
		else
			output << "Case #" << f + 1 << ": " << temp << endl;
	Partial_Break:
		;
	}
}