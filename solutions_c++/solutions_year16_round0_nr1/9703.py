#include <iostream>
#include<sstream>
#include<stdlib.h>
#include<stdio.h>
#include <fstream>
using namespace std;
int main()
{

	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("output_file.txt");

	
	string NS;
	int g = 0, h = 0, T = 0, N = 0;
	
	input >> T;
	
	while (T--)
	{
		bool x[10] = { 0 };
		int  NT = 0;
		input >> N;

		while (true)
		{
			if (N == 0) {
				output << "Case #" << h + 1 << ": " << "INSOMNIA" << endl;
				break;
			}
			

			
				NT = NT + N;
				stringstream ss;
				ss << NT;
				NS = ss.str();
				for (int i = 0; i<NS.size(); i++)
				{
					stringstream dd;
					dd << NS[i];
					int c = 0;
					dd >> c;
					x[c] = 1;

					
				
			}
				if (x[0] == 1 && x[1] == 1 && x[2] == 1 && x[3] == 1 && x[4] == 1 && x[5] == 1 && x[6] == 1 && x[7] == 1 && x[8] == 1 && x[9] == 1)
				{
					output << "Case #" << h + 1 << ": " << NT << endl;
					break;
				}

		}
		
		h++;



	}
}