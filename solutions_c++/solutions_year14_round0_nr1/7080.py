#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int main()
{
	int T=0;
	fin >> T;
	for (int t=1; t<=T; t++)
	{
		unsigned int cards[16];
		for (int i=0; i<16; i++)
			cards[i]=0;

		int choose=0;

		// first arrangmenet
		fin >> choose;
		unsigned int arrangement[4][4];
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				fin >> arrangement[i][j];
				if (i == choose-1)
					cards[arrangement[i][j]-1]+=1;
			}
		}

		// second arrangmenet
		fin >> choose;
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				fin >> arrangement[i][j];
				if (i == choose-1)
					cards[arrangement[i][j]-1]+=1;
			}
		}

		// analyze results
		int n2 = 0, answer = 0;
		for (int i=0; i<16; i++){
			if (cards[i]==2){
				n2 += 1;
				answer = i+1;
			}
		}

		// print output
		fout << "Case #" << t <<": ";
		if (n2==0) fout << "Volunteer cheated!";
		else if (n2==1) fout << answer;
		else fout << "Bad magician!";
		if (t!=T) fout << "\n";
	}
	return 0;
}