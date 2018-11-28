#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int debug = 0;
const double eps = 0.00001;
const double epsPLUS = 0.00001000001; // guard for roundoff

void readVector(vector<double>& v, int numBlocks) {
  v.reserve(numBlocks);
  double temp;
  for (int i = 0; i < numBlocks; i++) {
    cin >> temp;
    v.push_back(temp);
  }
}
void readAndSortVector(vector<double>& v, int numBlocks) {
  readVector(v, numBlocks);
  if (debug > 1) {
    cerr << "size=" << v.size() << "\n";
    for (int i = 0; i < v.size(); i++)
      cerr << v[i] << '\t';
    cerr << endl;
  }
  sort(v.begin(), v.end());
}

void print(const vector<double>& v) {
  for (int i = 0; i < v.size(); i++)
    cerr << v[i] << '\t';
  cerr << endl;
}

void doCase() {
  int numBlocks;
  cin >> numBlocks;
  vector<double> A, B;
  readAndSortVector(A, numBlocks);
  readAndSortVector(B, numBlocks);
  int win = 0, lose = 0, warWin = 0;
  int j = numBlocks-1;
  if (debug > 0) {
    cerr << "\n\n===============\n";
    print(A);
    print(B);
  }

  for (int i = numBlocks-1; i >= 0; i--) {
    if (A[i] > B[j]) { 
      warWin++;
      //      cerr << i << "," << j << ": " << A[i] << "," << B[j] << "\n";
    } else {
      j--;
    }
  }
  // tell B we have B+eps.  B will substitute smallest value
  // beat it with smallest block that will win
  for (int i = numBlocks-1; i >= 0; i--) {
    if (A[0] > B[i]) {
      cerr << " SHOULD WIN: " << A[0] << "," << B[B.size()-1] <<" " << A.size() <<"\n";
      win += A.size();
      break;
    }
    bool foundBigger = false;
    for (int j = 0; j < A.size(); j++)
      if (A[j] > B[0]) {
	B.erase(B.begin());
	A.erase(A.begin()+j);
	if (debug > 0) {
	  print(A);
	  print(B);
	}
	foundBigger = true;
	win++;
	break;
      }
    if (!foundBigger) {
      // Tell B you have B[max] - eps forcing him to give up his biggest
      for (int k = i; k >= 0; k--) {
	if (B[k] - B[k-1] > epsPLUS) {
	  B.erase(B.begin() + k); // delete kth element of B
	  A.erase(A.begin()); // give up smallest of ours
	  cerr << "take loss\n";
	  if (debug > 0) {
	    print(A);
	    print(B);
	  }
	  break;
	}
      }
    }
  }
  // remember there must be eps++ room in the sequence  or he will know
  // we are lying!!!
  // maybe testing 0.99999 is not enough, must check there wasn't
  // sequence like: 0.99999 0.99998 0.99997 with no room...Ugh
  printf("%d %d\n", win, warWin);
}

int main() {
  int numcases;
  cin >> numcases;
  for (int cases = 1; cases <= numcases; cases++) {
    printf("Case #%d: ", cases);
    doCase();
  }
}
