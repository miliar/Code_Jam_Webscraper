#include <iostream>
#include <fstream>


int main() {


	
	std::ifstream read;
	read.open("A-small-attempt1.in");

	std::ofstream write;
	write.open("output.txt");

	int x;

	read >>  x;

	for (int i = 0; i < x; i++) {
		int r1;
		int r2;
		int d1[4][4];
		int d2[4][4];
	

		read >> r1;

		for (int k = 0; k < 4; k++){
			for (int l = 0; l < 4; l++) {
				read >> d1[k][l];
			}
		}

		read >> r2;


		for (int k = 0; k < 4; k++){
			for (int l = 0; l < 4; l++) {
				read >> d2[k][l];
			}
		}

		int c = 0;
		int d = 0;
		for (int k = 0; k < 4; k++){
			for (int l = 0; l < 4; l++){
				if (d1[r1-1][k] == d2[r2-1][l]){
					c++;
					d = d1[r1-1][k];
				}
					
			}
		}

		
		
		if (c == 1)
			write << "Case #" << i+1 << ": " << d << std::endl;
		else if (c > 0)
			write << "Case #" << i+1 << ": Bad magician!" << std::endl;


		else if (c == 0)
			write << "Case #" << i+1 << ": Volunteer cheated!" << std::endl;


		
		
	}

	write.close();











}