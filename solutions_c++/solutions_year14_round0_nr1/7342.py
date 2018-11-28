#include <iostream>
#include <fstream>
using namespace std;

int caseNum, ans1, ans2;
int arrange1[4][4], arrange2[4][4];
ifstream fin;
ofstream fout;

void solveProblem()
{
	int count = 0;
	int res;
	fin >> ans1;
	ans1--;
	for( int i = 0; i < 4; ++i )
		for( int j = 0; j < 4; ++j )
			fin >> arrange1[i][j];
	fin >> ans2;
	ans2--;
	for( int i = 0; i < 4; ++i )
		for( int j = 0; j < 4; ++j )
			fin >> arrange2[i][j];
	for( int i = 0; i < 4; ++i )
		for( int j = 0; j < 4; ++j )
			if( arrange1[ans1][i] == arrange2[ans2][j] ){count++;res = i;}

	switch(count)
	{
	case 0: fout << "Volunteer cheated!\n";break;
	case 1: fout <<  arrange1[ans1][res] << '\n'; break;
	default: fout << "Bad magician!\n";
	}
}

int main()
{
	fin.open("input.in");
	fout.open("output.out");
	if( !fin ) { cout << "Error\n"; return -1;}
	fin >> caseNum;
	for( int i = 0; i < caseNum; ++i )
	{
		fout << "Case #" << i+1 << ": ";
		solveProblem();
	}
}