#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main() {
	ifstream fin("a.txt");
	ofstream fout("output.txt");
	int T; fin>>T;
	for(int t = 1;t<=T;t++) {
		int map1[17]; int map2[17];
		memset(map1,0,sizeof map1);
		memset(map2,0,sizeof map2);
		int firstGuess; fin>>firstGuess;
		int A[4][4];
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++)
			{
				fin>>A[i][j];
				if(i == firstGuess-1) map1[A[i][j]] = 1;
			}
		int secondGuess;fin>>secondGuess;
		
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++)
			{
				fin>>A[i][j];
				if(i == secondGuess-1) map2[A[i][j]] = 1;
			}
		int count = 0, res = -1;
		for(int i = 1;i<17;i++) {
				if (map1[i] == map2[i] && map1[i] == 1) { count++; res = i; }
		}

		fout<<"Case #"<<t<<": ";
		
			if(count == 1) fout<<res<<"\n";
		    else if(count == 0)
			fout<<"Volunteer cheated!\n";
			else fout<<"Bad magician!\n";
	}
	fin.close();
	fout.close();
}