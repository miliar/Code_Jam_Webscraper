#include <iostream>
#include <algorithm>
#include <string>
#include <utility>
using namespace std;

const int MAX_N = 130;
char A[MAX_N][MAX_N];

int di[4] = {-1,1,0,0};
int dj[4] = { 0,0,-1,1};
string dir = "^v<>";

void do_case(){
  int m,n;
  cin >> m >> n;
  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++)
      cin >> A[i][j];
  
  int ans = 0;
  
  for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
      if(A[i][j] == '.') continue;
      int status = 0;
      for(int k=0;k<4;k++){
        bool found = false;
        for(int l=1;;l++){
          int nI = i+di[k]*l;
          int nJ = j+dj[k]*l;
          if(!(0 <= nI && nI < m && 0 <= nJ && nJ < n))
            break;
          if(A[nI][nJ] != '.'){
            found = true;
            break;
          }
        }
        if(found && dir[k] == A[i][j]) status = 1;
        if(found && dir[k] != A[i][j] && status == 0) status = 2;
      }
      if(status == 0){
        cout << "IMPOSSIBLE" << endl;
        return;
      }
      if(status == 2) ans++;
    }
  }
  cout << ans << endl;
}

int main(){
  int T,C=1;
  cin >> T;
  while(T--){
    cout << "Case #" << C++ << ": ";
    do_case();
  }
  return 0;
}
