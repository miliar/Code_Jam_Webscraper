#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>

//Global Variables

//Main Function
int main(){
	std::ifstream in("/Users/Nikos/Downloads/D-small-attempt1.in");
	std::ofstream out("/Users/Nikos/Downloads/output.out");

	int T, X, R, C;
	std::string winner;
	in >> T;

	for (int i = 0; i < T; i++){
		winner = "RICHARD";
		//Input
		in >> X >> R >> C;

		//Editing
		switch (X){
		case 1:
			winner = "GABRIEL";
			break;
		case 2:
			if (R*C % 2 == 0){
				winner = "GABRIEL";
			}
			break;
		case 3:
			if (R*C % 6 == 0 || R*C == 9){
				winner = "GABRIEL";
			}
			break;
		case 4:
			if (R*C == 16 || R*C == 12){
				winner = "GABRIEL";
			}
			break;
		}

		//Output
		out << "Case #" << i + 1 << ": " << winner;
		if (i != T - 1){
			out << std::endl;
		}
	}

	in.close();
	out.close();
	system("pause");
	return 0;
}