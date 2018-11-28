#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>


using namespace std;


void alg() {
  int N, M;
  int T[100][100];
  int max_v[100] = {0}, max_h[100] = {0};
  
  cin >> N >> M;
  for (int i = 0; i < N*M; i++) {
    cin >> T[i/M][i%M];
    max_v[i%M] = T[i/M][i%M] > max_v[i%M] ? T[i/M][i%M] : max_v[i%M];
    max_h[i/M] = T[i/M][i%M] > max_h[i/M] ? T[i/M][i%M] : max_h[i/M];
  }
  
  for (int i = 0; i < N*M; i++) {
    if (T[i/M][i%M] < max_v[i%M] && T[i/M][i%M] < max_h[i/M]) {
      cout << "NO" << endl;
      return;
    }
  }
  
  cout << "YES" << endl;
}

int main() {
    int n_cases;
    cin >> n_cases;
    
    for (int test_case = 1; test_case <= n_cases; test_case++) {
      cout << "Case #" << test_case << ": ";
      alg();
    }

    return EXIT_SUCCESS;
}
