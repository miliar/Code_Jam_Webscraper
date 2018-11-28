//============================================================================
// Name        : magic_trick.cpp
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

    for(int i = 0; i < n ;i++){
    	int row1;
    	fin >> row1;
    	int dummy[4];
    	int cards1[4];
    	for(int j = 0; j < 4; j++){
    		for(int k = 0; k < 4; k++){
    			fin >> dummy[k];
    			if(j + 1 == row1){
    				cards1[k] = dummy[k];
    			}
    		}
    	}
    	int row2;
    	fin >> row2;
    	int cards2[4];
    	for(int j = 0; j < 4; j++){
    		for(int k = 0; k < 4; k++){
    			fin >> dummy[k];
    			if(j + 1 == row2){
    				cards2[k] = dummy[k];
    			}
    		}
    	}

    	//Compare
        int hit = 0;
        int num;
    	for(int j = 0; j < 4; j++){
    		for(int k = 0; k < 4; k++){
    			if(cards1[j] == cards2[k]){
    				hit++;
    				num = cards1[j];
    			}
    		}
    	}
    	fout << "Case #" << i+1;
    	if(hit == 0)
    		fout << ": Volunteer cheated!"<< endl;
    	else if(hit == 1)
    	    fout << ": " << num << endl;
    	else
    		fout << ": Bad magician!"<< endl;
    }
    cout << "Terminated" << endl;
    fin.close();
    fout.close();
  }

  else cout << "Unable to open file";

  return 0;
}
