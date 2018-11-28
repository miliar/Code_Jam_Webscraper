
#include<iostream>
#include<vector>


int min(int a, int b){
  if(a < b) return a;
  return b;
}

using namespace std;

int main(){
  int T;
  cin >> T;
  int N, M;
  for(int t = 1; t<= T; ++t){
    cin >> N >> M;
    vector<vector<int> > table(N, vector<int>(M, 0));
    for(int i = 0; i < N; ++i){
      for(int j = 0; j< M; ++j){
        cin >> table[i][j];
      }
    }

    vector<int> rows(N, 0);
    vector<int> columns(M, 0);
    int h;
    for(int i = 0; i < table.size(); ++i){
      h = 0;
      for(int j = 0; j < table[i].size(); ++j){
        if(table[i][j] > h) h = table[i][j];
      }
      rows[i] = h;
    }
    for(int j = 0; j < M; ++j){
      h = 0;
      for(int i = 0; i < N; ++i){
        if(table[i][j] > h) h = table[i][j];
      }
      columns[j] = h;
    }

    bool works = true;
    for(int i = 0; i < table.size(); ++i){
      for(int j = 0; j < table[i].size(); ++j){
        if(table[i][j] < min(rows[i], columns[j])){
          works = false;
          break;
        }
      }
      if(!works) break;
    }
    cout << "Case #" << t << ": ";
    if(works) cout << "YES" << endl;
    else cout << "NO" << endl;
  }


}


