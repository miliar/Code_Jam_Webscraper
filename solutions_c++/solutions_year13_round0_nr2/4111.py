#include <iostream>
#include <vector>
using namespace std;
static vector<vector<int> > lawn;
bool vertical(int col, int val){
  for(int i=0;i<lawn.size();i++){
    if(lawn[i][col] > val){
      return false;
    }
  }
  return true;
}
bool horizontal(int row, int val){
    for(int i=0;i<lawn[0].size();i++){
    if(lawn[row][i] > val){
      return false;
    }
  }
  return true;
}
int main(){
  int testcases;
  cin >> testcases;
  //cin.ignore()
  for(int i=1;i<=testcases;i++){
    //read rectangle into array
    int n, m;
    cin >> n >> m;
    lawn = vector<vector<int>  >(n, vector<int>(m));
    for(int j=0;j<n;j++){
      for(int k=0;k<m;k++){
        cin >> lawn[j][k];
      }
    }
    
    //for every 1, check if it is in a horizontal OR vertical row of 1s
    bool possible = true;
    for(int j=0;j<n;j++){
      for(int k=0;k<m;k++){
        possible &= (vertical(k, lawn[j][k]) || horizontal(j, lawn[j][k]));
        if(!possible){
          break;
        }
      }
      if(!possible){
        break;
      }
    }

    string possible_str = "YES";
    if(!possible){
      possible_str = "NO";
    }

    cout << "Case #" << i << ": " << possible_str << endl; 
  }
}