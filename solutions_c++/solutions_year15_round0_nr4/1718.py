#include <iostream>
#include <fstream>
//#include <vector>
//#include <string>
//#include <cstdlib>
//#include <unordered_map>
#include <algorithm>
using namespace std;

bool isGabriel(int X, int R, int C)
{
	if(R == 0 || C == 0) return false;
	if(X == 1) return true;
	if(X >= 7) return false;
	if((R*C)%X != 0) return false;
	if(min(R, C) < (X+1)/2) return false;
	if((X == 4 || X == 6) && min(R, C) == X/2) return false;
	if(max(R, C) < X) return false;
	return true;
}

int main()
{
	fstream  infile, outfile;
	infile.open("D-small-attempt0.in", ios::in);
	//infile.open("input.txt", ios::in);
	
	infile.seekg(0, ios::end);  
	if (infile.tellg() == 0) return 0;
	infile.seekg(0, ios::beg);
	
	outfile.open("output.txt", ios::out | ios::trunc);
	int i, nCase, X, R, C;
	infile >> nCase;
	//cout << nCase << endl;
	for(i = 0; i < nCase; i++)
	{
		infile >> X;
		infile >> R;
		infile >> C;
		
		if(isGabriel(X, R, C)) 
			outfile << "Case #" << i+1 << ": GABRIEL" << endl;
		else
			outfile << "Case #" << i+1 << ": RICHARD" << endl;
	}
	
	infile.close();
	outfile.close();
	
	return 0;
}
