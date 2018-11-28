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
//
//template < typename V >
//std::ostream& operator<< (std::ostream &out, const std::vector<V> &v) {
//  std::copy(v.begin(), v.end(), std::ostream_iterator<V>(out, " ") );
//  return out;
//}

std::ostream& operator<< (std::ostream &out, const std::vector<bool> &v) {
  std::copy(v.begin(), v.end(), std::ostream_iterator<bool>(out, "") );
  return out;
}

std::ostream& operator<< (std::ostream &out, const std::vector<uLL> &v) {
  std::copy(v.begin(), v.end(), std::ostream_iterator<uLL>(out, " ") );
  return out;
}

template < typename V >
std::ostream& operator<< (std::ostream &out, const std::set<V> &v) {
  std::copy(v.begin(), v.end(), std::ostream_iterator<V>(out, ", ") );
  return out;
}

uLL prime(uLL x)
{
  if (x < 2) return false;
  for(uLL i = 2;  i <= sqrt(x); i++) {
    if (( x % i) == 0) return i;
  }
  return 0;
}

vector<bool> convert(uLL x) {
  vector<bool> ret;
  while(x) {
    if (x&1)
      ret.push_back(true);
    else
      ret.push_back(false);
    x>>=1;
  }
//  reverse(ret.begin(),ret.end());
  return ret;
}

int main(int argc, char* argv[]) {
  google::ParseCommandLineFlags(&argc, &argv, true);
  std::ifstream in_file(FLAGS_in, ios::in);
  std::ofstream out_file(FLAGS_out, ios::out);
  int T;
  in_file >> T;

  out_file << "Case #1: " << "\r\n";
  int N, J;
  in_file >> N >> J;
  cout << "N " << N << " J " << J;
  vector<vector<uLL>> base_coeff;
  base_coeff.resize(9);
  FO(base, 2, 11) {
    base_coeff[base - 2].resize(N);
    FO(power, 0, N) {
      base_coeff[base - 2][N - power - 1] = pow(base, power);
    }
    cout << " base " << base << " coeff " << base_coeff[base - 2] << "\r\n";
  }
  vector<bool> num_vec(N, false);
  num_vec[0] = true;
  num_vec[N - 1] = true;
  vector<bool> mid_vec(N - 2, false);
  vector<vector<uLL>> divisors(J);
  int j = 0;
  FO(i, 0, pow(2, N) - 1) {
      mid_vec = convert(i + 1);
      cout << "mid vec " << mid_vec << "\r\n";
      std::copy(mid_vec.begin(), mid_vec.end() , num_vec.begin() + 1 );
      cout << "num_vec vec " << num_vec << "\r\n";
      bool is_good = true;
      divisors[j].erase(divisors[j].begin(), divisors[j].end());
      FO(base, 0, 9) {
        uLL num = std::inner_product(num_vec.begin(), num_vec.end(), base_coeff[base].begin() , 0.0);
        int div = prime(num);
        if (div == 0) {
          is_good = false;
          continue;
        } else {
          divisors[j].push_back(div);
        }
      }
      if (is_good) {
        out_file << num_vec << " " << divisors[j] << "\r\n";
        j++;
      }
      if (j == J)
        break;
  }


//
//    cout << "num_flip " <<  num_flip << "\r\n";
//    out_file << num_flip << "\r\n";

  return 0;
}
