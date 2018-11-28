#include <stdio.h>
#include <fstream>

using namespace std;

ifstream fin("3.in");
ofstream fout("3.out");

int p[1000];

int main(){
	int nCases;
	fin >> nCases;
	for(int t=1;t<=nCases;t++){
		int d;
		fin >> d;
		for(int i=0;i<d;i++){
			fin >> p[i];
		}
		
		int best = 10000;
		for(int eatTime = 1; eatTime<=1000; eatTime++){
			int nSpecial = 0;
			for(int i = 0; i<d; i++){
				nSpecial += (p[i]-1)/eatTime;
			}
			if(eatTime + nSpecial < best){
				best = eatTime + nSpecial;
			}
		}

		fout << "Case #" << t << ": " << best << endl;
	}
	return 0;
}