#include <iostream>

using namespace std;

int a[100][100];
int rmax[100], cmax[100];

int main(void){
  int T, N, M;
  cin >> T;
  for(int t = 0; t < T; ++t){
    cin >> N >> M;
    fill_n(rmax, N, 0);
    fill_n(cmax, M, 0);
    for(int i = 0; i < N; ++i)
      for(int j = 0; j < M; ++j){
        cin >> a[i][j];
        rmax[i] = max(rmax[i], a[i][j]);
        cmax[j] = max(cmax[j], a[i][j]);
      }

    bool ok = true;
    for(int i = 0; i < N; ++i)
      for(int j = 0; j < M; ++j)
        if(a[i][j] < rmax[i] && a[i][j] < cmax[j])
          ok = false;

    cout << "Case #" << t+1 << ": " << (ok ? "YES" : "NO") << endl;
  }

  return 0;
}
