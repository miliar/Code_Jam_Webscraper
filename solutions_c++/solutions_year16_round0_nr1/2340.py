//============================================================================
// Name        : A_sheep.cpp
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

    for(int i = 0; i < n ;i++){
    	int t,f;
    	bool dig[10] = {false};
    	fin >> t;
    	bool finished = false;
    	for(int mul = 1; (t!=0) && !finished; mul++){
    		f = t*mul;
    		for (int k = 1; k <= f ; k = k*10){
    			int tmp =  f / k;
				dig[(tmp % 10)] = true;
			}
			finished = true;
			for (int k = 0; k < 10; k++){
				finished = finished & dig[k];
			}
    	}
    	if (finished)
    		fout << "Case #" << i+1 << ": " << f << endl;
    	else
    		fout << "Case #" << i+1 << ": INSOMNIA" << endl;

    }
    cout << "Terminated" << endl;
    fin.close();
    fout.close();
  }

  else cout << "Unable to open file";

  return 0;
}
