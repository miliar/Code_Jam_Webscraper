#include <iostream>
using namespace std;

string dp[3][20];
int cnt[3][3][20];
string rps="PRS";

string doit(int w, int n) {
  if(n==0) {
    for(int w2=0; w2<3; w2++) cnt[w][w2][n]=(w==w2);
    return string(1,rps[w]);
  }
  int w1=w, w2=(w+1)%3;
  string& ret=dp[w][n];
  if(ret.size()) return ret;
  ret=min(doit(w1,n-1)+doit(w2,n-1), doit(w2,n-1)+doit(w1,n-1));
  for(int i=0; i<3; i++) cnt[w][i][n] = cnt[w1][i][n-1] + cnt[w2][i][n-1];
  return ret;
}

int main(void) {
  int T; cin >> T;
  for(int ts=1; ts<=T; ts++) {
    cout << "Case #" << ts << ": ";
    int n, R, P, S;
    cin >> n >> R >> P >> S;
    bool done=false;
    for(int w=0; w<3; w++) {
      doit(w,n);
      if(R==cnt[w][1][n] && P==cnt[w][0][n] && S==cnt[w][2][n]) {
        cout << doit(w,n) << endl;
        done=true;
      }
    }
    if(!done) cout << "IMPOSSIBLE" << endl;
  }
}
