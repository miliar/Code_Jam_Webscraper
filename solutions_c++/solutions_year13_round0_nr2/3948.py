//============================================================================
// Name        : lawmower.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	ifstream in("large.txt");
	ofstream out("large.out");
	int cases;
	in >> cases;
	for(int i = 1; i <= cases; ++i){
		int x, y;
		in >> x >>y;
		int mat[101][101];
		for(int i = 0; i < x; ++i){
			for(int j = 0; j < y; ++j){
				in >> mat[i][j];
			}
		}
		stringstream res;
		res << "Case #" << i << ": ";
		bool sol = false;
		for(int i = 0; i < x; ++i){
			for(int j = 0; j < y; ++j){
				//check hor
				bool hor = true;
				for(int h = 0 ; h < x; ++h){
					if(mat[h][j] > mat[i][j]){
						hor = false;
						break;
					}
				}
				bool ver = true;
				for(int v = 0; v < y; ++v){
					if(mat[i][v] > mat[i][j]){
						ver = false;
						break;
					}
				}
				if(!hor && !ver){
					sol = true;
					res << "NO";
					break;
				}
				//check vert
			}
			if(sol)
				break;
		}
		if(!sol)
			res <<"YES";
		out << res.str();
		if(i != cases)
			out <<"\n";

	}
	return 0;
}
