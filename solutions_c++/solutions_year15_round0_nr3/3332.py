#include "common.hpp"

using namespace std;

int sgn(int a) {
  return (a < 0) ? -1 : 1;
}

int const i_ = 2;
int const j_ = 3;
int const k_ = 4;

int const ij_  = k_;
int const ijk_ = -1;

int qmul(int a, int b) {
  static int qr[] = {
    1 ,  i_,  j_,  k_,
    i_, -1 ,  k_, -j_,
    j_, -k_, -1 ,  i_,
    k_,  j_, -i_, -1
  };

  int s  = sgn(a)*sgn(b);
  int aa = abs(a);
  int ab = abs(b);
  return s*qr[(aa-1)*4+ab-1];
}

int qinv(int a) {
  static int qr[] {
    1, -i_, -j_, -k_
  };
  int s  = sgn(a);
  int aa = abs(a);
  return s*qr[aa-1];
}

int readq() {
  char qc;
  cin >> qc;
  return qc-'i'+i_;
}

size_t L;
size_t X;
size_t N;

vectori quaternions{1, i_, j_, k_, -1, -i_, -j_, -k_};


void resetdic(dicii& d) {
  for(int q : quaternions)
    d[q] = -1;
}


void small_dataset(int t) {

  string line;
  bool r = false;

  cin >> ws;
  getline(cin, line);

  if(N >= 3) {
    stringstream buffer(line);
    string word;
    buffer >> word;
    
    vectori ds(N);
    for(size_t l=0; l<L; ++l)
      ds[l] = word[l]-'i'+i_;
  
    for(size_t x=1; x<X; ++x)
      copy(begin(ds), begin(ds)+L, begin(ds)+x*L);
  
    vectori sds;
    partial_sum(begin(ds), end(ds), back_inserter(sds), qmul);
    auto it = find(begin(sds), end(sds), i_);
    auto jt = find(it,         end(sds), ij_);
    r       = (it!=end(sds) && jt != end(sds) && sds.back() == ijk_);
  }
  cout << "Case #" << t << ": " << (r?"YES":"NO") << endl;
}


int main(int argc, char* argv[]) {

  string line;
  cin >> ws;
  getline(cin, line);
  stringstream buffer(line);

  uint T;
  buffer >> T;
  for(uint t=1; t<=T; ++t) {
    cin >> ws;
    getline(cin, line);
    stringstream buffer2(line);
    buffer2 >> L >> X;
    N    = L*X;
    cerr
      << "L = " << L << " "
      << "X = " << X << " "
      << "N = " << N << endl;
    small_dataset(t);
  }
}

