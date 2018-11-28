#include <iostream>
#include <assert.h>

using namespace std;

int main()
{
 // read input
 int T, N, M;
 int A[10][10];
 int Rmin[10], Cmin[10];
 int Rmax[10], Cmax[10];

 cin >> T;

 assert(T >= 1 && T <= 100);
 
 for (int i = 1; i <= T; ++i) {
  cin >> N >> M;
  assert(N >= 1 && N <= 10);
  assert(M >= 1 && M <= 10);

  for (int j = 0; j < N; ++j) {
   Rmin[j] = 1000;
   Rmax[j] = 0;
  }
  for (int k = 0; k < M; ++k) {
   Cmin[k] = 1000;
   Cmax[k] = 0;
  }

 //  cout << i << ":" << N << "x" << M << endl;

  for (int j = 0; j < N; ++j) {
   for (int k = 0; k < M; ++k) {
    cin >> A[j][k];
    assert(A[j][k] >= 1 && A[j][k] <= 2);
    Rmin[j] = min(Rmin[j], A[j][k]);
    Cmin[k] = min(Cmin[k], A[j][k]);
    Rmax[j] = max(Rmax[j], A[j][k]);
    Cmax[k] = max(Cmax[k], A[j][k]);
   } 
  }
  
  int g = 0;

  for (int j = 0; j < N; ++j) {
   for (int k = 0; k < M; ++k) {
    if (A[j][k] == Rmin[j] || A[j][k] == Cmin[k]) {
     if (Rmax[j] > Rmin[j] && Cmax[k] > Cmin[k]) {
      g++;
     }
    }
   }
  }

  cout << "Case #" << i << ": " << (g == 0 ? "YES" : "NO") << endl;
 }
}
