#include <iostream>
#include <algorithm>
using namespace std;

int n[2],a[2][4][4];

void solve(){
  int ans = -1;
  for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
      if(a[0][n[0]][i] == a[1][n[1]][j]){
        if(ans != -1){
          cout << "Bad magician!" << endl;
          return;
        } else ans = a[0][n[0]][i];
      }
    }
  }

  if(ans == -1) cout << "Volunteer cheated!" << endl;
  else cout << ans << endl;
}

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    for(int i=0;i<2;i++){
      cin >> n[i];
      n[i]--;
      for(int j=0;j<4;j++){
        for(int k=0;k<4;k++){
          cin >> a[i][j][k];
        }
      }
    }

    cout << "Case #" << t << ": " << flush;
    solve();
  }
}
