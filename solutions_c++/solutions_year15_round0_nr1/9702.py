#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>

//Global Variables
int Smax;

//Main Function
int main(){
	std::ifstream in("/Users/Nikos/Downloads/A-small-attempt1.in");
	std::ofstream out("/Users/Nikos/Downloads/output.out");

	int n, c, T;
	std::string line;
	in >> T;
	getline(in, line);

	for (int i = 0; i < T; i++){
		Smax = c = n = 0;

		//Input
		in >> Smax;
		getline(in, line);
		line.erase(0, 1);

		//Editing
		for (int j = 0; j < line.length(); j++){
			if (j > c && (int)line.at(j) - 48 != 0){
				n += j - c;
				c += n;
			}
			if ((int)line.at(j) - 48 != 0){
				c += (int)line.at(j) - 48;
			}
		}

		//Output
		out << "Case #" << i + 1 << ": " << n;
		if (i != T - 1){
			out << std::endl;
		}
	}

	in.close();
	out.close();
	system("pause");
	return EXIT_SUCCESS;
}