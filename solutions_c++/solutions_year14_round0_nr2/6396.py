#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


void main(){

	fstream fin, fout;

	fin.open("input.in", ios::binary | ios::in);
	fout.open("out.txt", ios::trunc | ios::out);

	int T;
	float C, F, X;

	double time;
	double nofactorytime;
	double factorytime;

	double cps;
	double cookies;

	fin >> T;

	for (int i = 1; i <= T; i++){
	
		fin >> C >> F >> X;
		cps = 2;
		cookies = 0;
		time = 0;
		while (cookies < X){

			nofactorytime = X / cps;
			factorytime = (C / cps) + (X / (cps + F));

			if (factorytime < nofactorytime){

				
				cookies -= C;
				time += C / cps;
				cps = cps + F;
			}
			else{
			
				cookies = X;

			}

		}
		time += X / cps;
	
		fout.precision(15);
		fout << fixed;
		fout << "Case #" << i << ": " << setprecision(6) << time << endl;
		
	}
	
	fin.close();
	fout.close();

}