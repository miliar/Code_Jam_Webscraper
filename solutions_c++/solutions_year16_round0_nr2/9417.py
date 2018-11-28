#include <stdio.h>
#include <fstream>
#include <iostream>
using namespace std;

int optimalFlipping(string pancakes) {
  int sign = (pancakes.at(0) == '+');
  int current = pancakes.at(0);
  int i = 1;
  int groups = 1;
  while (i < pancakes.size()) {
    if (pancakes.at(i) != current) {
      groups++;
    }
    current = pancakes.at(i);
    i++;
  }
  int total = groups + sign;
  return groups + (total%2) - 1;
}

int main(int argc, char const *argv[]) {
  string line;
  ifstream myfile ("RevengeOfThePancakes.in");
  ofstream outfile ("RevengeOfThePancakes.out");
  if (myfile.is_open() && outfile.is_open()){
    int T, N;
    int c = 1;
    getline(myfile, line);
    while ( getline(myfile,line) ){
      outfile << "Case #" << c << ": "<< optimalFlipping(line) << "\n";
      c++;
    }
    myfile.close();
    outfile.close();
  } else cout << "Unable to open file";

  return 0;
}
