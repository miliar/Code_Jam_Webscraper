#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main(){
	ifstream file;
	file.open("q1.txt");
	ofstream mfile;
	mfile.open("ee.txt");
	long long int T;
	file >> T;
	int I = 1;
	while (T--){
		long long int Smax;
		string q1;
		file >> Smax;
		file >> q1;
		//cout << "Smax " << Smax << "\n";
		//cout << "q1 " << q1 << "\n";
		long long int sumP,fri;
		sumP = 0; fri = 0;
		if (Smax == 0){
			mfile << "Case #" << I << ": " << fri << "\n";
			//cout << "tero \n"; 
			I++;
		}
		else {
			if ((int)q1[0]-48 == 0){
				fri++;
				sumP = fri+sumP;
			}
			else{
				sumP = (int)q1[0]-48+sumP;
			}
			for (int k = 1; k < Smax+1; k++){
				if (sumP >= k){
					sumP = sumP+(int)q1[k]-48;
				}
				else
				{
					long long int j = k-sumP;
					fri = fri + j;
					sumP = j + (int)q1[k]-48 + sumP;
				}
			}
			mfile << "Case #" << I << ": " << fri << "\n"; 
			I++;
		}
	}
}