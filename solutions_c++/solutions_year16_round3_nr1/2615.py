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
    char a_ch = 'A';
    in_file >> N;
//    string stringword;
//    in_file >> stringword;
//    cout << stringword;
    std::vector<unsigned> num_sen(N);
//    while(1) //Use a while loop, "i" isn't doing anything for you
//    {
//        //if comman not found find return string::npos
//
//        if (stringword.find(',')!=std::string::npos)
//        {
//            int value;
//            istringstream (stringword) >> value;
//
//            num_sen.push_back(value);
//
//           //Erase all element including comma
//            stringword.erase(0, stringword.find(',')+1);
//        }
//        else
//           break; //Come out of loop
//    }
//
    for (unsigned i = 0; i < N; i++) {
      in_file >> num_sen[i];
    }
    cout << num_sen << "\r\n";
    cout << " bye ";
    uLL sum_of_elems = std::accumulate(num_sen.begin(), num_sen.end(), 0);
    cout << "sum_of_elems "<< sum_of_elems << "\r\n";
    if (sum_of_elems % 2 == 1) {
      unsigned dist = std::distance(num_sen.begin(), std::max_element(num_sen.begin(),num_sen.end()));
      cout << "distacne " << dist  << "\r\n";
      num_sen[dist] -= 1;
      a_ch = 'A' + dist;
      out_file << a_ch << " ";
      sum_of_elems -= 1;
    }
    for (unsigned i = 0; i < sum_of_elems; i += 2) {
      unsigned dist = std::distance(num_sen.begin(), std::max_element(num_sen.begin(),num_sen.end()));
      cout << "distacne " << dist  << "\r\n";
      num_sen[dist] -= 1;
      a_ch = 'A' + dist;
      out_file << a_ch;
      dist = std::distance(num_sen.begin(), std::max_element(num_sen.begin(),num_sen.end()));
      cout << "distacne2 " << dist  << "\r\n";
      num_sen[dist] -= 1;
      a_ch = 'A' + dist;
            out_file << a_ch << " ";
    }
    out_file << "\r\n";
  }

  return 0;
}

