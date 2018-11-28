#include <iostream>
#include <cstring>

using namespace std;
int main() {
  int T;
  cin>>T;
  for (int t=1;t<=T;++t) {
    int N,M;
    cin>>N>>M;
    int dh[100][100];

    int mr[100] = {-1};
    int mc[100] = {-1};
    for (int r=0;r<N;++r) {
      for (int c=0;c<M;++c) {
        cin>>dh[r][c];
        mr[r] = max(mr[r], dh[r][c]);
        mc[c] = max(mc[c], dh[r][c]);
      }
    }

    int blah[100][100];
    memset(blah,100,sizeof(blah));
    bool good = true;
    for (int r=0;r<N;++r) {
      for (int c=0;c<M;++c) {
        blah[r][c] = min(mr[r], mc[c]);
        if (blah[r][c] != dh[r][c]) {
          good = false;
        }
      }
    }
    cout << "Case #" << t << ": " << (good ? "YES" : "NO") << endl;
  }
}
