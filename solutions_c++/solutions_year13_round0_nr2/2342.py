#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

string solve(vector<vector<int> >&, int N, int M);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    vector<vector<int> > lawn;
    int N, M;
    cin >> N >> M;
    for(int j = 0; j < N; j++) {
      vector<int> tmp;
      for(int k = 0; k < M; k++) {
	int h;
	cin >> h;
	tmp.push_back(h);
      }
      lawn.push_back(tmp);
    }
    string r = solve(lawn, N, M);
    cout << "Case #" << i+1 << ": " << r << endl;
  }
}

string solve(vector<vector<int> >& lawn, int N, int M){
  vector<int> max_row(N);
  vector<int> max_col(M);
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < M; j++) {
      if(lawn[i][j] > max_row[i]) max_row[i] = lawn[i][j];
      if(lawn[i][j] > max_col[j]) max_col[j] = lawn[i][j];
    }
  }
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < M; j++) {
      if(lawn[i][j] < max_row[i] && lawn[i][j] < max_col[j]) return "NO";
    }
  }
  return "YES";
}
