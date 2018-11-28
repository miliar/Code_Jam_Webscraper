#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

const int MAX_N = 1030;
string s[MAX_N];
int M,N;

int poww[10][10];

void do_case(){
  cin >> M >> N;
  for(int i=0;i<M;i++)
    cin >> s[i];

  int best = 0,ans = -1;
  for(int bM=0;bM<poww[N][M];bM++){
    set<string> S[MAX_N];
    int x = bM;
    for(int i=0;i<M;i++){
      int val = x % N;
      x /= N;
      for(int j=0;j<=s[i].length();j++) S[val].insert(s[i].substr(0,j));
    }
    int ctr = 0;
    bool bad = false;
    for(int i=0;i<N;i++){
      if(S[i].empty()) bad = true;
      ctr += S[i].size();
    }
    if(bad) continue;
    if(best < ctr) { best = ctr; ans = 0; }
    if(best == ctr) ans++;
  }
  cout << best << " " << ans << endl;
}

int main(){
  for(int i=1;i<10;i++){
    poww[i][0] = 1;
    for(int j=1;j<10;j++)
      poww[i][j] = poww[i][j-1] * i;
  }
  
  int T,C=1;
  cin >> T;
  while(T--){
    cout << "Case #" << C++ << ": ";
    do_case();
  }
  return 0;
}
