#include <iostream>
#include <vector>

using namespace std;

int main(void){
  int t;
  int n, m;

  cin >> t;

  for(int i=0;i<t;i++){
    cin >> n >> m;
    vector<vector<int> > lawn(n, vector<int> (m,0));

    for(int j=0;j<n;j++){
      for(int k=0;k<m;k++){
        cin >> lawn[j][k];
      }
    }
    bool bad = false;
    for(int j=0;j<n;j++){
      for(int k=0;k<m;k++){
        bool ok = true;
        bool ok2 = true;
        for(int l=0;l<n;l++){
          if(lawn[l][k] > lawn[j][k]){ ok = false; break;}
        }

        for(int l=0;l<m;l++){
          if(lawn[j][l] > lawn[j][k]){ ok2 = false; break;}
        }
        if(!ok2 && !ok){
          bad = true;
          break;
        }
      }
      if(bad) break;
    }
    if(bad){
      cout << "Case #" << i+1 << ": NO" << endl;
    }else{
      cout << "Case #" << i+1 << ": YES" << endl;
    }
  }
}
