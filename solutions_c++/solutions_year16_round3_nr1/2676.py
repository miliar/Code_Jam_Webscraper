//============================================================================
// Name        : A_Senate.cpp
// Author      : Jonas
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  int t;
  ifstream fin ("input.txt");
  ofstream fout ("output.txt");
  if (fin.is_open() && fout.is_open())
  {
    fin >> t;
    fout.precision(10);

    for(int i = 0; i < t ;i++){
    	int n;
    	fin >> n;
    	int p[n];

    	for(int j = 0; j < n; j++){
    		fin >> p[j];
    	}
    	int max;
    	fout << "Case #" << i+1 << ": ";
		while (true){
			max = 0;
			int sum = 0;
			int idx[2] = {-1,-1};
			for(int j = 0; j < n; j++){
				sum += p[j];
				if(p[j] >= max){
					idx[0] = idx [1];
					idx[1] = j;
					max = p[j];
				}
			}
			if(max == 0) break;
			if(sum == 3){
				fout << (char)(idx[1]+65);
				p[idx[1]] = p[idx[1]] -1;
			}
			else if((idx[0] != -1) & (p[idx[0]] >= p[idx[1]] - 1)){
				fout << (char)(idx[0]+65) << (char)(idx[1]+65);
				p[idx[0]] = p[idx[0]] -1;
				p[idx[1]] = p[idx[1]] -1;
			}
			else{
				fout << (char)(idx[1]+65) << (char)(idx[1]+65);
				p[idx[1]] = p[idx[1]] -2;
			}
			fout << " ";
		}
		fout << endl;



    }
    cout << "Terminated" << endl;
    fin.close();
    fout.close();
  }

  else cout << "Unable to open file";

  return 0;
}
