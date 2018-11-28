//============================================================================
// Name        : cookie.cpp
// Author      : joschy
// Version     :
// Copyright   : 
// Description :
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  int n;
  ifstream fin ("input.txt");
  ofstream fout ("output.txt");
  if (fin.is_open() && fout.is_open())
  {
    fin >> n;
    fout.precision(10);

    for(int i = 0; i < n ;i++){
    	double C,F,X;
    	fin >> C;
    	fin >> F;
    	fin >> X;


    	double time = X/2;
    	double newtime = X/2;
    	double t = 0;
    	for(int j = 0; time >= newtime ;j++){

    		time = newtime;
    		t = t + C/(2+j*F);
    		newtime = t + X/(2 + (j+1)*F);
    	}


    	fout << "Case #" << i+1 << ": " << time << endl;

    }
    cout << "Terminated" << endl;
    fin.close();
    fout.close();
  }

  else cout << "Unable to open file";

  return 0;
}
