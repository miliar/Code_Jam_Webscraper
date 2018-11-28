#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;
  cin >> T;
  
  for(int tc = 1 ; tc <= T ; tc++){
    bool candidate[2][16+1];
    memset(candidate, false, sizeof(candidate));
    
    int r;
    int grid[4][4];
    for(int k = 0 ; k < 2 ; k++){
      cin >> r;
      for(int i = 0 ; i < 4 ; i++)
	for(int j = 0 ; j < 4 ; j++) cin >> grid[i][j];

      for(int j = 0 ; j < 4 ; j++){
	candidate[k][ grid[r-1][j] ] = true;
      }      
    }
    
    vector<int> ans;
    for(int i = 1 ; i <= 16 ; i++)
      if(candidate[0][i] && candidate[1][i]) ans.push_back(i);
    
    cout << "Case #" << tc << ": ";
    if((int)ans.size() == 1) cout << ans[0] << endl;
    else if(ans.size() > 1) cout << "Bad magician!" << endl;
    else cout << "Volunteer cheated!" << endl;
  }
  
  return 0;
}
