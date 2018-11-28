#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
using namespace std;

#define MAX_HEIGHT 101;
#define MIN_HEIGHT 0;
string input = "B-small-attempt2.in";
string input1 = "test";
string output = "B-small-attempt2.out";

int main()
{
  ifstream infile(input.c_str());
  ofstream outfile(output.c_str());
  
  string line, word;
  int t, n, m;
  // Get the T from the input file
  getline(infile, line);
  t = atoi(line.c_str());
  int test = 1;
  while (test <= t) {
    // Get the N and M from the input file
    getline(infile, line);
    istringstream stream(line);
    stream >> word;
    n = atoi(word.c_str());
    stream >> word;
    m = atoi(word.c_str());
    int *design = new int[n*m]();
    int *reality = new int[n*m]();
    // Get the desired grass patterns from the input file,
    // also do the cutting with the lawnmower in the horizontal direction
    for (int i = 0; i < n; i++) {
      getline(infile, line);
      istringstream stream(line);
      int max_height = MIN_HEIGHT;
      // Get the pattern at ith line
      for (int j = 0; j < m; j++) {
	stream >> word;
	design[i*m+j] = atoi(word.c_str());
	if (design[i*m+j] > max_height) 
	  max_height = design[i*m+j];
      }
      // Do the cutting at ith line
      for (int j = 0; j < m; j++) {
	reality[i*m+j] = max_height;
	cout << reality[i*m+j];
      }
      cout << endl;
    }
    
    bool possible = true;
    for (int j = 0; j < m; j++) {
      bool equal = true;
      int min_height = MAX_HEIGHT;
      int max_height = MIN_HEIGHT;
      for (int i = 0; i < n; i++) {
	if (design[i*m+j] != reality[i*m+j]) 
	  equal = false;
	if (design[i*m+j] > max_height)
	  max_height = design[i*m+j];
	if (design[i*m+j] < min_height)
	  min_height = design[i*m+j];
      }
      if (equal == false && max_height != min_height) {
	possible = false;
	break;
      }
    }
    
    if (possible == true) {
      outfile << "Case #";
      outfile << test;
      outfile << ": YES";
      outfile << "\n";
      cout << "YES" << endl;
    } else {
      outfile << "Case #";
      outfile << test;
      outfile << ": NO";
      outfile << "\n";
      cout << "NO" << endl;
    }
    delete design;
    delete reality;
    test++;
  }
}
