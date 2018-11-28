#include <iostream>
#include <string>
#include <stdio.h>
#include<fstream>
#include <sstream>

using namespace std;

int main() {

	ifstream input;
	input.open("B-large.in");
	ofstream output;
	output.open("output_file.txt");
	int c;
	input >> c;
	string cake;
	

	for (int i = 0; i < c; i++)
	{
		int step = 0;
		input >> cake;
		for (int j = 0; j < cake.length(); j++)
		{
			
			if (j + 1 == cake.length()) {
			
				if (cake[j] == '-') { output << "Case #" << i + 1 << ": " << step + 1<<endl; }
				else{ output << "Case #" << i + 1 << ": " << step << endl; }
				break;
			}
			if (cake[j] != cake[j+1]) {
				step++;
				}
			else {}
		}
	}

	input.close();
	output.close();

	return 0;
}