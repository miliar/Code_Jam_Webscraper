
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>



int main()
{

	int T;


	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");


	infile >> T;
//	char out[1000];

	for (int i = 1; i <= T; i++) {
		std::cout << i << std::endl;
		std::string input = "";
		std::string output = "";
		std::string tmpout = "";

		infile >> input;

		for (int j = 0; j < input.length(); j++) {
			//output.append(input.begin()+j,input.begin()+j+1);
			tmpout = output + input[j];
			if (tmpout.compare((input[j] + output)) > 0)
				output = tmpout;
			else
				output = input[j] + output;


		}
//		std::cout << output << "" << std::endl;
//		std::cout << input<<""<<input.length()<<std::endl;
		outfile << "case #" << i << ": " << output << std::endl;


	}
	getchar();
}