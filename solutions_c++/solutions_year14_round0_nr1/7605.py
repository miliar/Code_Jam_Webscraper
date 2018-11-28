#include <iostream>

using namespace std;

void solve(){
  int ans1, ans2;
  int card1[4][4], card2[4][4];
  
  cin >> ans1;
  --ans1;
  for(int i=0;i<4;++i){
    for(int j=0;j<4;++j){
      cin >> card1[i][j];
    }
  }
  
  cin >> ans2;
  --ans2;
  for(int i=0;i<4;++i){
    for(int j=0;j<4;++j){
      cin >> card2[i][j];
    }
  }
  
  int pos1[4];
  
  for(int i=0;i<4;++i)
    pos1[i] = card1[ans1][i];
  
  int pos2[4];
  
  for(int i=0;i<4;++i)
    pos2[i] = card2[ans2][i];
  
  //find intersection of pos1 and pos2
  
  int s=0;
  int ans;
  for(int i=0;i<4;++i){
    for(int j=0;j<4;++j){
      if(pos1[i] == pos2[j]) {
        ++s;
        ans = pos1[i];
      }
    }
  }
  
  if(s == 0) cout << "Volunteer cheated!\n";
  else if(s == 1) cout << ans << endl;
  else cout << "Bad magician!\n";
}

int main(){
  int ncase;
  cin >> ncase;
  for(int i=0;i<ncase;++i){
    std::cout << "Case #" << i+1 << ": ";
    
    solve();
  }
}