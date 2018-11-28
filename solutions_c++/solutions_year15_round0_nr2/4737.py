// Code Jam 2015 QR
// Infinite House of Pancakes
// Author: Max Pflueger

#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

// Calculate moves for a split solution
int moves(const vector<int>& P, const vector<int>& splits) {
  // Number of special minutes
  int s = 0;
  for (auto si: splits) {
    s += si;
  }

  // Normal minutes
  int m = 1;
  for (int i=0; i < P.size(); i++) {
    int j = ceil((float) P[i] / (float) (splits[i] + 1));
    if (j > m) m = j;
  }

  //cout << s << " + " << m << "=" << m + s << endl;
  return m + s;
}

// Solve the Infinite House of Pancakes problem
int solveIHOP(const vector<int>& P) {
  int D = P.size();
  vector<int> split(D, 0);
  vector<int> curr_P = P;

  vector<int> best_split = split;
  int best_time = moves(P, best_split);

  int n = 0;
  while (n < best_time) {
    // Find the highest stack
    int tallest = 0;
    int height = curr_P[0];
    for (int i=1; i<D; i++) {
      if (curr_P[i] > height) {
        height = curr_P[i];
        tallest = i;
      }
    }

    // Add a split for the highest stack
    n += 1;
    split[tallest] += 1;
    curr_P[tallest] = ceil((float) P[tallest] / (float) (split[tallest] + 1));

    if (moves(P, split) < best_time) {
      best_time = moves(P, split);
      best_split = split;
    }
  }

  //cout << "Best Split:";
  //for (auto i: best_split) {
  //  cout << " " << i;
  //}
  //cout << endl;
  return best_time;
}

// Read n int values out of the file
vector<int> readVals(fstream* fs, int n) {
  vector<int> vals;
  int x;

  vals.resize(n);
  for (int i=0; i < n; i++) {
    *fs >> x;
    vals[i] = x;
  }
  return vals;
}

void readCase(fstream* fs, int case_num) {
  int D = 0;
  *fs >> D;

  vector<int> P = readVals(fs, D);
  if (P.size() != D) {
    cerr << "Error\n";
    return;
  }

  int turns = solveIHOP(P);

  cout << "Case #" << case_num << ": " << turns << endl;
}

int main(int argc, char** argv) {
  // Check number of args
  if (argc < 2) {
    cout << "Please supply an input file.\n";
    return -1;
  }

  // Open the input file (read only)
  fstream fs;
  fs.open(argv[1], fstream::in);

  int cases;
  fs >> cases;
  for (int i=0; i<cases; i++) {
    readCase(&fs, i+1);
  }
}
