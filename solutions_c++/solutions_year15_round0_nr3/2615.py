#include<iostream>
#include<fstream>
#include<cstdio>
#include<string>
using namespace std;
int T, L,X;
string SSS,S;
int N[10000];
int C[9][9];
int Mul(int i, int j){ return C[i][j]; }
int main()
{
	C[0][0] = 3; C[1][0] = 6; C[2][0] = 1; C[3][0] = 8;
	C[0][1] = 2; C[1][1] = 3; C[2][1] = 8; C[3][1] = 7;
	C[0][2] = 7; C[1][2] = 0; C[2][2] = 3; C[3][2] = 6;
	C[0][3] = 8; C[1][3] = 7; C[2][3] = 6; C[3][3] = 5;
	C[0][5] = 0; C[1][5] = 1; C[2][5] = 2; C[3][5] = 3;
	C[0][6] = 1; C[1][6] = 8; C[2][6] = 5; C[3][6] = 2;
	C[0][7] = 6; C[1][7] = 5; C[2][7] = 0; C[3][7] = 1;
	C[0][8] = 5; C[1][8] = 2; C[2][8] = 7; C[3][8] = 0;
	for (int i = 5; i <= 8; i++){
		for (int j = 0; j <= 8; j++){
			if (j == 4)continue;
			C[i][j] = 8 - C[8 - i][j];
		}
	}
	ifstream fin("C:/Users/Toshifumi/C-small-attempt1.in");
	ofstream fout("C:/Users/Toshifumi/out.txt");
	fin >> T;
	for (int C = 1; C <= T; C++){
		S = "";
		fin >> L >> X;
		fin >> SSS;
		for (int i = 0; i < X; i++)S += SSS;
		for (int i = 0; i < S.length(); i++){
			if (S[i] == 'i')N[i] = 6;
			else if (S[i] == 'j')N[i] = 7;
			else N[i] = 8;
		}
		bool F = true;
		int Ba = 0;
		if (S.length() < 3)F = false;
		else{
			int kkk = N[Ba];
			Ba++;
			while (kkk != 6){
				kkk = Mul(kkk, N[Ba]);
				Ba++;
				if (Ba == S.length()){
					F = false;
					goto next;
				}
			}
			kkk = N[Ba];
			Ba++;
			if (Ba == S.length()){
				F = false;
				goto next;
			}
			while (kkk != 7){
				kkk = Mul(kkk, N[Ba]);
				Ba++;
				if (Ba == S.length()){
					F = false;
					goto next;
				}
			}
			kkk = N[Ba];
			for (int i = Ba + 1; i < S.length(); i++){
				kkk = Mul(kkk, N[i]);
			}
			if (kkk != 8)F = false;
		next:;

		}
		fout << "Case #" << C << ": ";
		if (F)fout << "YES\n";
		else fout << "NO\n";
	}
	return 0;
}