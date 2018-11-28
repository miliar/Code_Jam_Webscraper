#include<fstream>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
	ifstream fin("SmallB0.in");
	ofstream fout("SmallBSol.out");
	int runs, A, B, K, Bin, lot, wins;
	fin >> runs;
  for(int i = 0; i < runs; i++){
    wins = 0;
		fin >> A >> Bin >> K;
	  A--;
	  Bin--;
	  for(A; A >= 0; A--){
	    for(B = Bin; B >= 0; B--){
	      if((A & B) < K){
	        wins++;
	      }
      }
	  }
	  fout << "Case #" << i+1 << ": " << wins << endl;
	}
	return 0;
}
