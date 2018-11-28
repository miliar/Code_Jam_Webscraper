#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);


  const int64_t R=0, P=1, S=2;
  int64_t T;
  cin >> T;

  vector<vector<string>> results(13,vector<string>(3));
  results[0][R]='R';
  results[0][P]='P';
  results[0][S]='S';
  for(int64_t i=1;i<=12;i++) {
    if(results[i-1][R] <= results[i-1][S]) {
      results[i][R]=results[i-1][R]+results[i-1][S];
    } else {
      results[i][R]=results[i-1][S]+results[i-1][R];
    }
    if(results[i-1][P] <= results[i-1][R]) {
      results[i][P]=results[i-1][P]+results[i-1][R];
    } else {
      results[i][P]=results[i-1][R]+results[i-1][P];
    }
    if(results[i-1][P] <= results[i-1][S]) {
      results[i][S]=results[i-1][P]+results[i-1][S];
    } else {
      results[i][S]=results[i-1][S]+results[i-1][P];
    }
  }

  vector<vector<vector<int64_t>>> counts(13,vector<vector<int64_t>>(3, vector<int64_t>(3)));
  for(int64_t i=0;i<=12;i++) {
    for(int64_t j=0;j<3;j++) {
      for(int64_t k=0;k<results[i][j].size();k++) {
        if(results[i][j][k] == 'R') {
          counts[i][j][R]++;
        } else if(results[i][j][k] == 'P') {
          counts[i][j][P]++;
        } else {
          counts[i][j][S]++;
        }
      }
    }
  }

  for(int64_t t=1;t<=T;t++) {
    int64_t n, r, p, s;
    cin >> n >> r >> p >> s;
    cout << "Case #" << t << ": ";
    if(counts[n][P][P] == p && counts[n][P][R] == r && counts[n][P][S] == s) {
      cout << results[n][P] << "\n";
    } else if(counts[n][R][P] == p && counts[n][R][R] == r && counts[n][R][S] == s) {
      cout << results[n][R] << "\n";
    } else if(counts[n][S][P] == p && counts[n][S][R] == r && counts[n][S][S] == s) {
      cout << results[n][S] << "\n";
    } else {
      cout << "IMPOSSIBLE\n";
    }
  }
  
  return 0;
}

