#include <iostream>
#include <fstream>

using namespace std;

int processData(int Smax, string Si) {
  int sum = 0;
  int min = 0;
  for(int i=0; i < Smax+1; ++i) {
    if(sum < i) {
      int diff = i - sum;
      sum += diff;
      min += diff;
    }
    sum += (int) Si[i] - '0';
  }

  return min;
}

int main() { 
  ifstream infile;
  ofstream outfile;
  string s;
  int T;
  int Smax;
  string Si;

  infile.open("A-small-attempt0.in");
  outfile.open("output.txt");

  if(!infile.is_open()) {
    cerr << "file not open." << endl;
    exit(0);
  }

  getline(infile, s);
  T = stoi(s, nullptr, 10);

  // Real puzzle begins here
  // T cases
  for(int c=0; c<T; ++c) {
    infile >> s;
    Smax = std::stoi(s, nullptr, 10);
    infile >> Si;
    int min = processData(Smax, Si);
    outfile << "Case #" << c+1 << ": " << min << endl;
  }

  infile.close();
  outfile.close();
}
