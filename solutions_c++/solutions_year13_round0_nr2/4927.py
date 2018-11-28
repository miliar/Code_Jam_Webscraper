#include <iostream>
#include <vector>
#include <string>

using namespace std;

string
solve(vector<vector<int> > field) {
  bool possible = true;
  string result = "YES";
  
  for(int r = 0; possible && (r < field.size()); r++) {
    for(int c = 0; possible && (c < field[r].size()); c++) {
      int nv = 0, nh = 0;
      for(int i = 0; i < field.size(); i++) {
        if(field[i][c] <= field[r][c]) {
          nv++;
        }
      }
      for(int i = 0; i < field[r].size(); i++) {
        if(field[r][i] <= field[r][c]) {
          nh++;
        }
      }
      
      possible &= (nh == field[r].size()) | (nv == field.size());
    }
  }
  
  if(!possible) {
    result = "NO";
  }
  
  return result;
}

int
main() {
  int T;
  cin >> T;
  
  for(int i = 1; i <=T; i++) {
    vector<vector<int> > field;
    int N, M;
    cin >> N >> M;
    
    for(int r = 0; r < N; r++) {
      vector<int> row(M);
      
      for(int c = 0; c < M; c++) {
//        int f;
        
        cin >> row[c];
        
//        row[c] = f;
      }
      
      field.push_back(row);
    }
    
    cout << "Case #" << i << ": " << solve(field) << endl;
  }
  
  return 0;
}
