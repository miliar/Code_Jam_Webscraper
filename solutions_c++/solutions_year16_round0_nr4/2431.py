#include <algorithm>
#include <bits/stdc++.h>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iomanip>      // std::setprecision
#include <iostream>
#include <iterator>
#include <string>
#include <fstream>
#include <math.h>

#include <gflags/gflags.h>
using namespace std;
typedef long long LL;
typedef unsigned long long uLL;
#define FO(i,a,b) for (int (i) = (a); (i) < (b); ++(i))
double PI = 3.141592653;

DEFINE_string(in, "-", "YModel to generate PCA Volume Signature for");
DEFINE_string(out, "-", "YModel to generate PCA Volume Signature for");

template < typename V >
std::ostream& operator<< (std::ostream &out, const std::vector<V> &v) {
  std::copy(v.begin(), v.end(), std::ostream_iterator<V>(out, " ") );
  return out;
}

//printf("%0.8lf\n",ans);
int main(int argc, char* argv[]) {
  google::ParseCommandLineFlags(&argc, &argv, true);
  std::ifstream in_file(FLAGS_in, ios::in);
  std::ofstream out_file(FLAGS_out, ios::out);
  int T;
  in_file >> T;
  FO(t, 1, T + 1) {
    cout << t;
    out_file << "Case #" << t << ": ";
    int K, C, S;
    in_file >> K >> C >> S;
    vector<int> sol(S);
    //Looking at the first K tiles would solve the issues: if the first tile
    // in the original K tiles is gold, then it will all be G.
    // If the first tile is L, then the first K tiles will show the full
    // original sequence
    std::iota(sol.begin(), sol.end(), 1);
    out_file << sol << "\r\n";
  }

  return 0;
}
