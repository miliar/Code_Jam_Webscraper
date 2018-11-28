#include <iostream>
#include <fstream>

using namespace std;

int main(){
  ifstream in("C:/CodeJam/2/B-large.in");
  ofstream out("C:/CodeJam/2/res_long.txt");
  unsigned int T;
  in >> T;
  for (unsigned int t = 0; t < T; ++t){
    unsigned int N,M;
    in >> N >> M;
    unsigned int* board = new unsigned int[N*M];
    for (unsigned int n = 0; n < N; ++n)
      for (unsigned int m = 0; m < M; ++m)
        in >> board[n*M + m];
    // Находим максимумы
    unsigned int* rows = new unsigned int[N];
    unsigned int* cols = new unsigned int[M];
    for (unsigned int i = 0; i < N; ++i){
      unsigned int ans = 0;
      for (unsigned int j = 0; j < M; ++j)
        ans = max(ans, board[i*M+j]);
      rows[i] = ans;
    }
    for (unsigned int j = 0; j < M; ++j){
      unsigned int ans = 0;
      for (unsigned int i = 0; i < N; ++i)
        ans = max(ans, board[i*M+j]);
      cols[j] = ans;
    }
    bool over = true;
    for (unsigned int n = 0; n < N; ++n){
      for (unsigned int m = 0; m < M; ++m)
        if ((board[n*M+m] < rows[n]) && (board[n*M+m] < cols[m])){
          over = false;
          break;
        }
      if (!over) break;
    }
    out << "Case #" << t+1<< ": " << (over ? "YES" : "NO") << endl;
    delete []board;
    delete []rows;
    delete []cols;
  }
  in.close();
  out.close();
}