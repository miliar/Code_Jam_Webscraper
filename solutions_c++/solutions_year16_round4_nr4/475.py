#include <iostream>
using namespace std;

int N;
int grid[5][5];

bool doit(int people=0, int machines=0) {
  if((people+1) == 1<<N) return true;
  bool any=false;
  for(int i=0; i<N; i++) if(people&(1<<i)); else {
    for(int j=0; j<N; j++) if(grid[i][j]) if(machines&(1<<j)); else {
      if(!doit(people|(1<<i), machines|(1<<j))) return false;
      any=true;
    }
  }
  return any;
}

int main(void) {
  int T; cin >> T;
  for(int ts=1; ts<=T; ts++) {
    cin >> N;
    for(int i=0; i<N; i++) for(int j=0; j<N; j++) {
      char c; cin >> c;
      grid[i][j] = (c=='1');
    }
    int best=N*N;
    for(int msk=0; msk<(1<<(N*N)); msk++) {
      int cnt=0;
      for(int i=0; i<N; i++) for(int j=0; j<N; j++) {
        int k = i*N+j;
        if(msk&(1<<k)) { cnt++; grid[i][j]++; }
      }
      if(doit()) {
        //if(cnt<best) cout << cnt << " " << msk << endl;
        best=min(best,cnt);
      }
      for(int i=0; i<N; i++) for(int j=0; j<N; j++) {
        int k = i*N+j;
        if(msk&(1<<k)) { cnt++; grid[i][j]--; }
      }
    }
    cout << "Case #" << ts << ": " << best << endl;
  }
}
