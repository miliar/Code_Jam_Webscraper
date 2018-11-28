//============================================================================
// Name        : war.cpp
// Author      : joschy
// Version     :
// Copyright   : 
// Description :
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main () {
  int t;
  ifstream fin ("input.txt");
  ofstream fout ("output.txt");
  if (fin.is_open() && fout.is_open())
  {
    fin >> t;

    for(int i = 0; i < t ;i++){
    	int n;
    	fin >> n;
    	double naomi[n];
    	double ken[n];
    	for(int j = 0 ; j < n; j++)
    		fin >> naomi[j];
    	for(int j = 0 ; j < n; j++)
    	    fin >> ken[j];
    	sort(naomi, naomi + n);
    	sort(ken, ken + n);

    	int y = 0;
    	for(int j = 0; j < n; j++){
    		if(naomi[j] > ken[y])
    			y++;
    	}

    	int zn = 0;
    	for(int j = 0; j < n; j++){
    		if(ken[j] > naomi[zn])
    			zn++;
    	}



    	fout << "Case #" << i+1 << ": " << y << " " << n - zn << endl;

    }
    cout << "Terminated" << endl;
    fin.close();
    fout.close();
  }

  else cout << "Unable to open file";

  return 0;
}
