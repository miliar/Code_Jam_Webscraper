#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int main(){
	ifstream ifile("three.txt");
	ofstream ofile("threeout.txt");
	int count;
	int size;
	
	ifile >> size;
	
	int low, up;
	
	for(int i = 0; i < size; i++){
		count = 0;
		ifile >> low >> up;
		
		for(int j = low; j <= up; j++){
			// check if square
			int sq = sqrt(j);
			if(sq * sq != j){continue;}
			
			// check if palindrome 
			string jfor = static_cast<ostringstream*>( &(ostringstream() << j) )->str();
			string jback = string ( jfor.rbegin(), jfor.rend() );
			
			if(jfor != jback){continue;}
			// check if palindrome
			string sfor = static_cast<ostringstream*>( &(ostringstream() << sq) )->str();
			string sback = string ( sfor.rbegin(), sfor.rend() );
			
			if(sfor != sback){continue;}

			count ++;
		}
		ofile << "Case #" << i + 1 << ": " << count << endl;
	}
	
	return 0;
}
