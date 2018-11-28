#include <fstream>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <iterator>

using namespace std;
ifstream in("in");
ofstream out("out");
int casei, ncase;
ostream &writeCase() {
  return out<<"Case #"<<++casei<<": ";
}
void writeCaseYESNO(bool yes) {
  writeCase() << (yes ? "YES" : "NO") << '\n';
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
void Show(int *v, int N) {
  copy(v,v+N,ostream_iterator<int>(cerr," "));
  cerr<<'\n';
}

/// N rows by M cols.
int N, M;
int NM;
int const maxN = 100;
int lawnbuf[maxN*maxN]; // max needed: N=M=100
#define lawn(n, m) lawnbuf[(n)*M+(m)]

/**
   say we're looking at the shortest height patch which isn't yet explained by a cut

   then at that position, either a row or column cut was made at that height.

   how do we know which cut was used? actually, we don't care.
*/

/// actual max heights for row, col in lawn
int rowmaxht[maxN];
int colmaxht[maxN];


void PrepLawn() {
  NM = N*M;
  fill(rowmaxht, rowmaxht+maxN, 0);
  fill(colmaxht, colmaxht+maxN, 0);
  for (int r = 0; r<N; ++r)
    for (int c = 0; c<M; ++c) {
      int h = lawn(r, c);
      MaxEq(rowmaxht[r], h);
      MaxEq(colmaxht[c], h);
    }
}

bool CanMow() {
  PrepLawn();
  for (int r = 0; r<N; ++r)
    for (int c = 0; c<M; ++c) {
      int h = lawn(r, c);
      bool canrowcut = h==rowmaxht[r];
      bool cancolcut = h==colmaxht[c];
      if (!(canrowcut || cancolcut ))
        return false;
    }
  return true;
}

int main() {
  in>>ncase;
  for (int i = 0; i<ncase; ++i) {
    in>>N;
    in>>M;
    for (int r = 0; r<N; ++r)
      for (int c = 0; c<M; ++c)
        in>>lawn(r, c);
    writeCaseYESNO(CanMow());
  }
  InEof();
}
