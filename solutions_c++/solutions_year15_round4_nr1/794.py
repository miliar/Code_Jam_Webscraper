#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<utility>

using namespace std;

int main(void) {
  int64_t T;
  cin >> T;
  for(int64_t t=1;t<=T;t++) {
    int64_t r,c;
    cin >> r >> c;
    vector<vector<char>> board(r,vector<char>(c,'.'));
    for(int64_t i=0;i<r;i++) {
      for(int64_t j=0;j<c;j++) {
        cin >> board[i][j];
      }
    }
    int64_t cnt=0;
    bool impossible=false;
    for(int64_t i=0;i<r;i++) {
      for(int64_t j=0;j<c;j++) {
        bool isbad=false;
        if(board[i][j] == '^') {
          isbad=true;
          for(int64_t k=i-1;k>=0;k--) {
            if(board[k][j] != '.') {
              isbad=false;
              break;
            }
          }
        } else if(board[i][j] == '>') {
          isbad=true;
          for(int64_t k=j+1;k<c;k++) {
            if(board[i][k] != '.') {
              isbad=false;
              break;
            }
          }
        } else if(board[i][j] == '<') {
          isbad=true;
          for(int64_t k=j-1;k>=0;k--) {
            if(board[i][k] != '.') {
              isbad=false;
              break;
            }
          }
        } else if(board[i][j] == 'v') {
          isbad=true;
          for(int64_t k=i+1;k<r;k++) {
            if(board[k][j] != '.') {
              isbad=false;
              break;
            }
          }
        }
        if(isbad) {
          cnt++;
          bool foundmatch=false;
          for(int64_t k=i-1;k>=0;k--) {
            if(board[k][j] != '.') {
              foundmatch=true;
              break;
            }
          }
          for(int64_t k=j+1;k<c;k++) {
            if(board[i][k] != '.') {
              foundmatch=true;
              break;
            }
          }
          for(int64_t k=j-1;k>=0;k--) {
            if(board[i][k] != '.') {
              foundmatch=true;
              break;
            }
          }
          for(int64_t k=i+1;k<r;k++) {
            if(board[k][j] != '.') {
              foundmatch=true;
              break;
            }
          }
          if(!foundmatch) {
            impossible=true;
            break;
          }
        }
      }
      if(impossible) break;
    }
    if(impossible) {
      cout << "Case #" << t << ": IMPOSSIBLE\n";
    } else {
      cout << "Case #" << t << ": " << cnt << "\n";
    }
  }
  return 0;
}

