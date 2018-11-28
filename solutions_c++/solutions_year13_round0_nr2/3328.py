#include <iostream>
#include <fstream>

using namespace std;

int lawn[101][101];
int current_lawn[101][101];

int Max_In_Row(int i, int n, int m);
int Max_In_Column(int j, int n, int m);


int main() {
  ifstream infile;
  ofstream outfile;
  infile.open("test.txt");
  if(infile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }


  outfile.open("Codejamtest.txt");
  if(outfile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }


  int num_tests, n, m, patch_height, break_bool;

  infile >> num_tests;

  for(int z = 0; z < num_tests; z++) {
    infile >> n >> m;
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) {
	infile >> patch_height;
	lawn[i][j] = patch_height;
	current_lawn[i][j] = 100;
      }
    }

    break_bool = 0;
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) {
	if((lawn[i][j] != Max_In_Row(i, n, m)) && (lawn[i][j] != Max_In_Column(j, n, m))) {
	  break_bool = 1;
	  break;
	}
      }
      if(break_bool == 1) break;
    }
    
    if(break_bool == 1) {
      outfile << "Case #" << z << ": NO" << endl;
    } else {
      outfile << "Case #" << z << ": YES" << endl;
    }
  }

}

int Max_In_Row(int i, int n, int m) {
  int max = -1;
  for(int z = 0; z < m; z++) {
    if(lawn[i][z] > max) max = lawn[i][z];
  }
  return max;
} 

int Max_In_Column(int j, int n, int m) {
  int max = -1;
  for(int z = 0; z < n; z++) {
    if(lawn[z][j] > max) max = lawn[z][j];
  }
  return max;
}


