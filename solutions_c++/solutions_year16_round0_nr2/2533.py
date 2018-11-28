#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	ifstream infile("B-large.in");
	ofstream outfile("B-large.out");

	int length;
	string input;
	infile >> length;
	vector <string> inputs;

	int flipCount = 0;

	for (int i = 0; i < length; ++i)
	{
		infile >> input;
		inputs.push_back(input);
	}

	for(int i = 0; i < length; i++){
		input = inputs[i];
		char current = input[0];
		flipCount = 0;
		for (int j = 0; j < input.length(); ++j)
		{
			if(input[j] != current){
				if(current == '+'){
					current = '-';
					flipCount++;
				}
				else if(current == '-'){
					current = '+';
					flipCount++;
				}
			}
		}
		if(current == '-'){
			flipCount++;
		}
		outfile << "Case #"<< i+1 << ": " << flipCount << endl;
	}

	return 0;
}