#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

//istream& fin = cin;
//ifstream fin ("A-sample.txt");
ifstream fin ("A-small-attempt0.in");
//ifstream fin ("A-large.in");
ofstream fout ("A-small-attempt0.out");
//ofstream fout ("A-large.out");
//ostream& fout = cout;

const char* MULTI_SOL = "Bad magician!";
const char* NO_SOL = "Volunteer cheated!";

int main()
{
	int N;
	int cards[2][4][4];
	int row[2];
	
	fin >> N;
	for(int n=1; n<=N; n++)
	{
		for(int k=0; k<2; k++)
		{
			fin >> row[k];
			row[k]--; // convert to 0-based index
			for(int i=0; i<4; i++)
			{
				for(int j=0; j<4; j++)
				{
					fin >> cards[k][i][j];
				}
			}
		}
		
		int nSol = 0;
		int sol;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				int card0 = cards[0][row[0]][i];
				int card1 = cards[1][row[1]][j];
				// cout << card0 << " " << card1 << endl;
				if(card0 == card1)
				{
					nSol++;
					sol = card0;
				}
			}
		}
		
		fout << "Case #" << n << ": ";
		switch(nSol)
		{
			case 0: fout << NO_SOL; break;
			case 1: fout << sol; break;
			default: fout << MULTI_SOL;
		}
		fout << endl;
	}
	
	return 0;
}

