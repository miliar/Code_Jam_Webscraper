#include <iostream>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

int N, M;
string S[1009];
string st;

int A[1009];
set<string> P[109];

int maxValue;
int maxCount;

void recurse(int k, int bucket) {
  A[k] = bucket;
  
  /*
  for (int i = 0; i <= k; ++i)
    cout << A[i] << " ";
  cout << endl;
  */
  
  if (k == M - 1) {
    // check all buckets are non-empty
    for (int i = 0; i < N; ++i)
      P[i].clear();
    for (int w = 0; w < M; ++w) {
      int myBucket = A[w];
      for (unsigned int i = 0; i <= S[w].length(); ++i)
        P[myBucket].insert(S[w].substr(0, i));
    }
    
    // count
    bool ok = true;
    int myCount = 0;
    for (int i = 0; i < N; ++i) {
      if (P[i].empty()) {
        ok = false;
        break;
      }
      myCount += P[i].size();
    }
    if (!ok) return;
    if (maxValue == myCount) maxCount++;
    if (maxValue < myCount) {
      maxValue = myCount;
      maxCount = 1;
    }
  }
  else
    for (int i = 0; i < N; ++i)
      recurse(k + 1, i);
}

int main()
{
  int T;
  cin >> T;
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // init
    maxValue = 0;
    maxCount = 0;
    
    // input
    cin >> M >> N;
    getline(cin, st);
    for (int i = 0; i < M; ++i)
      getline(cin, S[i]);
    
    // recurse
    for (int i = 0; i < N; ++i)
      recurse(0, i);
    
    cout << "Case #" << Ti << ": " << maxValue << " " << maxCount << endl;
  }
  return 0;
}