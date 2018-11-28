//============================================================================
// Name        : B_pancake.cpp
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
  int n;
  ifstream fin ("input.txt");
  ofstream fout ("output.txt");
  if (fin.is_open() && fout.is_open())
  {
    fin >> n;
    fout.precision(10);
    char dummy[100];
    fin.getline(dummy,1);

    for(int i = 0; i < n ;i++){
    	char x[200], cur;
    	fin.getline(x,200);
    	cur = x[0];
    	int c = 0;
    	for(int j = 0; j < 100 && (x[j] == '+' || x[j] == '-')  ; j++){
    		if (cur != x[j]){
    			c++;
    			cur = x[j];
    		}
    	}
    	if(cur == '-')
    		c++;

    	fout << "Case #" << i+1 << ": " << c << endl;

    }
    cout << "Terminated" << endl;
    fin.close();
    fout.close();
  }

  else cout << "Unable to open file";

  return 0;
}
