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
  std::copy(v.begin(), v.end(), std::ostream_iterator<V>(out, ", ") );
  return out;
}
template < typename V >
std::ostream& operator<< (std::ostream &out, const std::set<V> &v) {
  std::copy(v.begin(), v.end(), std::ostream_iterator<V>(out, ", ") );
  return out;
}

int main(int argc, char* argv[]) {
  google::ParseCommandLineFlags(&argc, &argv, true);
  std::ifstream in_file(FLAGS_in, ios::in);
  std::ofstream out_file(FLAGS_out, ios::out);
  int T;
  in_file >> T;
  FO(t, 1, T + 1) {
    out_file << "Case #" << t << ": ";
    set<int> seen;
    uLL N;
//    uLL num_mul = 0;
    in_file >> N;
    if (N == 0) {
      out_file << "INSOMNIA" << "\r\n";
      continue;
    }
    uLL i = 1;
//    uLL num_z = 0;
//    while (N % 10 == 0) {
//      seen.insert(0);
//      N /= 10;
//      num_z ++;
//    }
    uLL prev_N = 0;
    while (seen.size() < 10) {
      uLL tmp_N =  prev_N + N;
      prev_N = tmp_N;
      cout << " new N " << tmp_N << " , seen digits " << seen << "\r\n";
//      num_mul ++;
      while (tmp_N > 0) {
        int digit = tmp_N % 10;
        tmp_N /= 10;
        seen.insert(digit);
      }
      i++;
    }
//    uLL result = prev_N;
//    cout << "num_mul " <<  num_mul << "\r\n";
    out_file << prev_N << "\r\n";
  }

  return 0;
}
