#include <fstream>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <iterator>
#include <cstdint>
#include <cmath>
#include <iomanip>

using namespace std;
typedef uint64_t U64;
typedef unsigned N;

typedef N U;

ifstream in("in");
ofstream out("out");
N casei, ncase;
ostream &writeCase() {
  return out<<"Case #"<<++casei<<": ";
}
void writeCaseYESNO(bool yes) {
  writeCase() << (yes ? "YES" : "NO") << '\n';
}
template <class C>
void writeCase(C const& c) {
  writeCase() << c << '\n';
}
void InEof() {
  char c;
  assert(!(in>>c));
  assert(in.eof());
}
void MaxEq(int &i, int bigger) {
  if (i<bigger)
    i = bigger;
}
void Show(U *v, int N) {
  copy(v, v+N, ostream_iterator<U>(cerr," "));
  cerr<<'\n';
}


N n;
N const maxN=1000*1000;
U us;
U them[maxN];

U solve() {
  if (n==0) return 0;
  sort(them,them+n);
  U last=them[n-1];
  if (us<=1) return n;
  //TODO: bound/collapse runs removing duplicates?
  cerr<<"start="<<us<<' ';
  //Show(them,n);
  N togrow=0;
  for (N i=0; i<n; ++i) {
    N grow=0;
    N tar=them[i];
    U uspre=us;
    while (us<=tar) {
      ++grow;
      us*=2;--us; // add
    }
    N remain=n-i;
    if (grow >= remain) {
      cerr<<"no point growing @ "<<i+1<<" of "<<n<<" - would take "<<grow<<" to go from "<<uspre<<" to "<<us<<" to eat "<<tar<<" and only "<<remain<<" to delete i...n-1: moves="<<togrow+remain<<'\n';
      return togrow+remain; // delete rest instead of adding
    }
    us+=tar;
    togrow+=grow;
  }
  cerr<<"ate everything: moves="<<togrow<<" to "<<us<<'\n';
  return togrow; // never reached
}


int main() {
  in>>ncase;
  for (N i = 0; i<ncase; ++i) {
    in >> us;
    in >> n;
    for (N j = 0; j<n; ++j)
      in >> them[j];
    writeCase() << solve() <<'\n';
  }
  InEof();
}
