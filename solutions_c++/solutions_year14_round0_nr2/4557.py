#include <iostream>
#include <fstream>
#include <iomanip>


int main() {


	
	std::ifstream read;
	read.open("B-large.in");

	std::ofstream write;
	write.open("output.txt");

	int x;

	read >>  x;

	for (int i = 0; i < x; i++) {
		double C, F, X;

		read >> C;
		read >> F;
		read >> X;

		double rate = 2;

		double time = 0;

		double fin = 0;
		double buy = 0;

		while (true){
			if ((X / rate) < (C / rate) + (X / (rate + F))){
				time += X / rate;
				break;
			}
			else{
				time += C / rate;
				rate += F;
			}
		}
		

		write << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(8) << time << std::endl;
		
	}


	write.close();











}