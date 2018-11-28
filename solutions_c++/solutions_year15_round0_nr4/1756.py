#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int T, X, R, C;
int main()
{
	ifstream fin("C:/Users/Toshifumi/D-small-attempt0.in");
	ofstream fout("C:/Users/Toshifumi/out.txt");
	fin >> T;
	for (int c = 1; c <= T; c++){
		fin >> X >> R >> C;
		bool F;
		if (X == 1)F = true;
		else if (X == 2){
			if (R % 2 == 0 || C % 2 == 0)F = true;
			else F = false;
		}
		else if (X == 3){
			if ((R*C) % 3 == 0){
				if (R == 1 || C == 1)F = false;
				else F = true;
			}
			else F = false;
		}
		else{
			if ((R*C) % 4 == 0){
				if (R <= 2 || C <= 2)F = false;
				else F = true;
			}
			else F = false;
		}
		fout << "Case #" << c << ": ";
		if (!F)fout << "RICHARD\n";
		else fout << "GABRIEL\n";
	}
	return 0;
}