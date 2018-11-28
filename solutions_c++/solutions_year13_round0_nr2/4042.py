#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int Q;
  cin >> Q;
  for(int q=0;q<Q;q++) {
    if(q == 8){
      q = q;
    }
    cout << "Case #" << q+1 << ": ";
    int n,m;
    cin >> n >> m;
    vector<vector<int> > a(n, vector<int> (m));
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
        cin >> a[i][j];
      }
    }
    int f = 1;
    for(int k=1;k<=100 && f;k++){
      for(int i=0;i<n && f;i++){
        for(int j=0;j<m && f;j++){
          if (a[i][j] == k) {
            int ff = 1;
            for(int ii=0;ii<n && ff;ii++){
              ff = a[ii][j]<=k;
            }
            for(int ii=0;ii<n && ff;ii++){
              a[ii][j] = 0;
            }
            int fff = 1;
            for(int jj=0;jj<m && fff;jj++){
              fff = a[i][jj]<=k;
            }
            for(int jj=0;jj<m && fff;jj++){
              a[i][jj] = 0;
            }
            if (!ff && !fff)
              f = 0;
          }
        }
      }
    }
    if (f){
      cout << "YES\n";
    }
    else {
      cout << "NO\n";
    }
  }
  return 0;
}