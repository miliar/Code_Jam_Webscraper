#include <bits/stdc++.h>
using namespace std;

const int INF = 1<<28;
int N;
vector<vector<string> > word;

int main() {
  int T; cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    cin >> N; cin.ignore();
    word = vector<vector<string> >(N);
    map<string, int> B;
    for(int i = 0; i < N; ++i) {
      string s; getline(cin, s);
      for(stringstream ss(s); ss >> s; ) {
        B[s] |= 1 << i;
        word[i].push_back(s);
      }
    }
    int res = INF;
    for(int b = 0; b < (1<<N); ++b) {
      if(!(b >> 0 & 1) && (b >> 1 & 1)); else continue;
      int sum = 0;
      for(map<string, int>::iterator it = B.begin();
          it != B.end(); ++it) {
        if((b & it->second) && (~b & it->second)) ++sum;
      }
      res = min(res, sum);
    }
    cout << res << endl;
  }
  return 0;
}
