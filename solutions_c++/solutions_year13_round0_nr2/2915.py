#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;


bool sweepHorVer(int temp[][100], int a, int b, int y, int x){

	int element = temp[a][b];


	bool horBlock = false;
	bool verBlock = false;


	for(int i=0;i<x;i++){

		if(temp[a][i] > element) {horBlock = true;break;}	
		
	}



	for(int i=0;i<y;i++){

		if(temp[i][b] > element) {verBlock = true;break;}	
		
	}

	if(horBlock && verBlock) return false; else return true;

}

bool isValidPattern(int temp[][100], int a, int b){

	

	for(int i=0;i<a;i++){

		for(int j=0;j<b;j++){


			if(!sweepHorVer(temp, i, j, a, b)){
				return false;
			}


		}

	}

	return true;
	

}


int main(){
	
	
	
	ifstream file("B-large.in");
	ofstream outfile("output.txt");




	int total;
	file >> total;



	for(int i=0;i<total;i++){


		int a;
		file >> a;

		int b;
		file >> b;


		
		int temp[100][100];
					

			for(int j=0;j<a;j++){

				for(int k=0;k<b;k++){

					file >> temp[j][k];
				
				}

			}


			

			if(isValidPattern(temp, a, b)){
				outfile << "Case #"<<(i+1)<<": YES"<< endl;
			}
			else
			{
				outfile << "Case #"<<(i+1)<<": NO"<< endl;
			}
			

			

	}

	

	


}