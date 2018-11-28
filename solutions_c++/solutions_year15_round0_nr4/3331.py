#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;



int main(){
	
	ifstream file("test.in");
	ofstream outfile("test2.out");
	
	int iterations;
	file >> iterations;
	
	
	
	for (int i = 0; i<iterations; i++){
		
		int X,R,C;
		
		file >> X >> R >> C;
		
		if (X%4 == 1 || (X%4 == 2 && (R*C)%2 == 0) || (X%4 == 3 & ((R*C) == 6 || (R*C) == 9 || (R*C) == 12)) ||(X%4 == 0 && (R*C) >= 12)){
			outfile << "Case #" << i+1 << ": GABRIEL" << endl; 
		}
		
		else
			outfile << "Case #" << i+1 << ": RICHARD" << endl; 
		
	}	
}
