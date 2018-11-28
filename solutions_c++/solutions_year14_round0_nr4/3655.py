#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
  int cases=0;
  cin >> cases;
  int casenum=0;
  while (casenum < cases) {
    casenum++;
    int numBlocks=0;
    cin >> numBlocks;
    vector<double> nBlocks;
    double nextVal=0.0;
    for (int i=1; i<=numBlocks; i++) {
      cin >> nextVal;
      nBlocks.push_back(nextVal);
    }
    vector<double> kBlocks;
    for (int i=1; i<=numBlocks; i++) {
      cin >> nextVal;
      kBlocks.push_back(nextVal);
    }
    int warPoints=0;
    int n=0;
    int k=0;
    sort(nBlocks.begin(),nBlocks.end());
    sort(kBlocks.begin(),kBlocks.end());
    while (k < numBlocks) {
      if (nBlocks[n] < kBlocks[k]) {
        n++;
        k++;
      } else {
        warPoints++;
        k++;
      }
    }
    int decPoints=0;
    n=0;
    k=0;
    while (n < numBlocks) {
      if (nBlocks[n] > kBlocks[k]) {
        decPoints++;
        n++;
        k++;
      } else {
        n++;
      }
    }
    cout << "Case #" << casenum << ": " << decPoints << " " << warPoints << endl;
  }
  return 0;
}

