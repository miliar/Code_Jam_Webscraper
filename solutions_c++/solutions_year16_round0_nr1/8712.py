#include <iostream>
#include <string>
#include <stdio.h>
#include<fstream>
#include <sstream>

using namespace std;

int main() {

	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("output_file.txt");
	int c;
	input >> c;
	int n;
	int num;

	for (int i = 0; i < c; i++)
	{
		int j = 1;
		
		input >> n;
		num = n;
		bool bit[10] = { 0 };
		while (true)
		{

			

			string nstr;

			if (n == 0) {
				output << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
				break;
			}
			num = n*j;
			stringstream ss;
			ss << num;
			nstr = ss.str();
			for (size_t k = 0; k < nstr.length(); k++)
			{
				if (nstr[k] == '0') { bit[0] = 1; }
				if (nstr[k] == '1') { bit[1] = 1; }
				if (nstr[k] == '2') { bit[2] = 1; }
				if (nstr[k] == '3') { bit[3] = 1; }
				if (nstr[k] == '4') { bit[4] = 1; }
				if (nstr[k] == '5') { bit[5] = 1; }
				if (nstr[k] == '6') { bit[6] = 1; }
				if (nstr[k] == '7') { bit[7] = 1; }
				if (nstr[k] == '8') { bit[8] = 1; }
				if (nstr[k] == '9') { bit[9] = 1; }

			}

			if (bit[0] == 1 && bit[1] == 1 && bit[2] == 1 && bit[3] == 1 && bit[4] == 1 && bit[5] == 1 && bit[6] == 1 && bit[7] == 1 && bit[8] == 1 && bit[9] == 1)

			{
				output << "Case #" << i+1  << ": " << num << endl;
				break;
			}

			j++;
		}
	}
	fclose(stdout);
}