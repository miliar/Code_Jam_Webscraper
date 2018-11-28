#include <iostream>
#include <vector>

using namespace std;

int solve(vector<int>& S) {
  int N = 0, nsum = 0;
  for (int s = 0; s < S.size(); s++) {
    int delta = s - nsum - N;
    N += (delta > 0 ? delta : 0);
    nsum += S[s];
  }
  return N;
}

int main(int argc, char *argv[]) {
  int ntest;
  cin >> ntest;
  for (int T = 0; T < ntest; T++) {
    int maxS;
    cin >> maxS;
    string ns;
    cin >> ns;    
    vector<int> S;
    for (int i=0; i <= maxS; i++) {
      S.push_back(ns[i]-'0');
    }
    cout << "Case #"<< (T+1) <<": " << solve(S) <<endl;
  }
  return 0;
}
