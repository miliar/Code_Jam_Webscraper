#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int v[100];
int ans[100][100]; // act, enr

int main() {

  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    int E, R, N;
    cin >> E >> R >> N;
    for (int i = 0; i < N; i++)
      cin >> v[i];


    for (int e = 0; e <= E; e++)
      ans[N-1][e] = v[N-1]*e;
    for (int a = N-2; a>=0; a--) {
      for (int e = 0; e <= E; e++) {
	ans[a][e] = 0;
	for (int used = 0; used <= e; used++) {
	  int after = e - used + R;
	  if (after > E)
	    after = E;
	  ans[a][e] = max(ans[a][e],ans[a+1][after] + used*v[a]);
	}
      }
    }

    cout << "Case #"<< test << ": " << ans[0][E] << endl; 
  }

  return 0;
}
