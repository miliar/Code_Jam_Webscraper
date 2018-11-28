#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#define N 4
#define O 'O'
#define X 'X'
#define T 'T'

using namespace std;

char check1(const vector<string>& data){
  for(int i=0; i<N; ++i){
    if((data[i][0] == O || data[i][0] == T) &&
       (data[i][1] == O || data[i][1] == T) &&
       (data[i][2] == O || data[i][2] == T) &&
       (data[i][3] == O || data[i][3] == T)) return O;
    if((data[i][0] == X || data[i][0] == T) &&
       (data[i][1] == X || data[i][1] == T) &&
       (data[i][2] == X || data[i][2] == T) &&
       (data[i][3] == X || data[i][3] == T)) return X;
    if((data[0][i] == O || data[0][i] == T) &&
       (data[1][i] == O || data[1][i] == T) &&
       (data[2][i] == O || data[2][i] == T) &&
       (data[3][i] == O || data[3][i] == T)) return O;
    if((data[0][i] == X || data[0][i] == T) &&
       (data[1][i] == X || data[1][i] == T) &&
       (data[2][i] == X || data[2][i] == T) &&
       (data[3][i] == X || data[3][i] == T)) return X;
  }
  if((data[0][0] == O || data[0][0] == T) &&
     (data[1][1] == O || data[1][1] == T) &&
     (data[2][2] == O || data[2][2] == T) &&
     (data[3][3] == O || data[3][3] == T)) return O;
  if((data[0][0] == X || data[0][0] == T) &&
     (data[1][1] == X || data[1][1] == T) &&
     (data[2][2] == X || data[2][2] == T) &&
     (data[3][3] == X || data[3][3] == T)) return X;
  if((data[0][3] == O || data[0][3] == T) &&
     (data[1][2] == O || data[1][2] == T) &&
     (data[2][1] == O || data[2][1] == T) &&
     (data[3][0] == O || data[3][0] == T)) return O;
  if((data[0][3] == X || data[0][3] == T) &&
     (data[1][2] == X || data[1][2] == T) &&
     (data[2][1] == X || data[2][1] == T) &&
     (data[3][0] == X || data[3][0] == T)) return X;
  return T;
}

bool check2(const vector<string>& data){
  for(int i=0; i<N; ++i){
    for(int j=0; j<N; ++j){
      if(data[i][j] == '.') return false;
    }
  }
  return true;
}

string solve(const vector<string>& data){
  char c = check1(data);
  if(c != T){
    if(c == O) return "O won";
    else return "X won";
  }
  if(check2(data)) return "Draw";
  else return "Game has not completed";
}

int main(){
  int n;
  string s;
  vector<string> data;
  cin >> n;
  for(int i=0; i<n; ++i){
    for(int j=0; j<N; ++j){
      cin >> s;
      data.push_back(s);
    }
    cout << "Case #" << i+1 << ": " << solve(data) << endl;
    data.clear();
  }
  return 0;
}
