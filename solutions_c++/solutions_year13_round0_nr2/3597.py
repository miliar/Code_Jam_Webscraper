#include <stdio.h>
#include <iostream>
#include <fstream>

// OPTIONAL
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char *argv[])
{
  ifstream read("input.in");
  ofstream write;
  write.open ("output.out");
  // STARTS HERE
  int n, N, M, b[100][100], c;
  bool p, q;
  read >> n;
  for (int case_no = 1; case_no <= n; ++case_no) {
    read >> N >> M;
    for (int y = 0; y < N; ++y) {
      for (int x = 0; x < M; ++x) {
        read >> b[x][y];
      } // end for x 
    } // end for y 
    for (int y = 0; y < N; ++y) {
      for (int x = 0; x < M; ++x) {
        p = q = true;
        c = b[x][y];
        for (int i = 0; i < N; ++i) {
          if(b[x][i] > c)
            p = false;
        } // end for i 
        for (int i = 0; i < M; ++i) {
          if(b[i][y] > c)
            q = false;
        } // end for i 
        if (!p && !q)
        { x = M; y = N; }
      } // end for x 
    } // end for y 
    // END HERE
    write << "Case #" << case_no << ": ";
    // ANSWER HERE
    if(p || q)
      write << "YES" << endl;
    else
      write << "NO" << endl;
  } // end for case_no 
  return 0;
}
