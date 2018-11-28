//------------------------------------------------------------------------------
// Copyright (c) 2013 Mineyuki Iwasaki. All rights reserved.
//------------------------------------------------------------------------------
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define LOG(f,...) fprintf(stderr, f, __VA_ARGS__)
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  // Loop
  int N, M;
  char buffer[100][100];
  int Nmax[100];
  int Nmin[100];
  int Mmax[100];
  int Mmin[100];
  bool result = false;
  bool ok = true;
  for (int t = 0; t != T; ++t) {
    result = false;
    ok = true;
    // Input size.
    scanf("%d", &N);
    scanf("%d", &M);

    // Input board.
    for (int n = 0; n != N; ++n) {
      for (int m = 0; m != M; ++m) {
        scanf("%d", &buffer[n][m]);
      }
    }

    // Analysis.
    if (N == 1 || M == 1) {
      result = true;
      ok = true;
    } else {
      // Make max/min map.
      for (int n = 0; n != N; ++n) {
        Nmax[n] = 1;
        Nmin[n] = 100;
        for (int m = 0; m != M; ++m) {
          if (Nmax[n] < buffer[n][m]) {
            Nmax[n] = buffer[n][m];
          }
          if (Nmin[n] > buffer[n][m]) {
            Nmin[n] = buffer[n][m];
          }
        }
      }
      for (int m = 0; m != M; ++m) {
        Mmax[m] = 1;
        Mmin[m] = 100;
        for (int n = 0; n != N; ++n) {
          if (Mmax[m] < buffer[n][m]) {
            Mmax[m] = buffer[n][m];
          }
          if (Mmin[m] > buffer[n][m]) {
            Mmin[m] = buffer[n][m];
          }
        }
      }
      /*
      for (int n = 0; n != N; ++n) {
        LOG("N[%d](%d,%d) ",n, Nmax[n], Nmin[n]);
      }
      LOG("\n");
      for (int m = 0; m != M; ++m) {
        LOG("M[%d](%d,%d) ",m, Mmax[m], Mmin[m]);
      }
      LOG("\n");
      */

      // Check all cell.
      for (int n = 0; n != N; ++n) {
        for (int m = 0; m != M; ++m) {
          if (buffer[n][m] == Nmax[n] || buffer[n][m] == Mmax[m]) {
            // OK
          } else {
            result = true;
            ok = false;
            break;
          }
        }
        if (result) {
          break;
        }
      }
    }

    // Result.
    if (ok) {
      printf("Case #%d: YES\n", t+1);
    } else {
      printf("Case #%d: NO\n", t+1);
    }
  }
  return 0;
}
