#include <fstream>
#include <string>
#include <iostream>
#include <cassert>
using namespace std;

ifstream in;
ofstream out;

int N,M;
int lawn[1000][1000];

int maxrow[1000];
int maxcol[1000];
bool solve() {
  int i,j;
  for (i=0;i<N;++i) {
    int max=0;
    for (int j=0;j<M;++j)
      if (lawn[i][j]>max) max=lawn[i][j];
    maxrow[i] = max;
  }
  for (j=0;j<M;++j) {
    int max=0;
    for (int i=0;i<N;++i)
      if (lawn[i][j]>max) max=lawn[i][j];
    maxcol[j] = max;
  }
  for (i=0;i<N;++i)
    for (j=0;j<M;++j) {
      if (!(lawn[i][j]==maxrow[i] || lawn[i][j]==maxcol[j]))
	return false;
    }
  return true;
}

int main(int argc, char *argv[]) {
  assert(argc==3 || argc==4);
  string name=string(argv[1])+"-"+argv[2];
  if (argc==4)
    name += string("-")+argv[3];
  in.open((name+".in").c_str());
  assert(in);
  out.open((name+".out").c_str());
  assert(out);

  int T;
  in >> T;
  for (int t=1;t<=T;++t) {
    cout<<t<<endl;
    in>>N>>M;
    for (int i=0;i<N;++i) {
      for (int j=0;j<M;++j) {
	in>>lawn[i][j];
      }
    }
    out<<"Case #"<<t<<": ";
    if (solve())
      out<<"YES"<<endl;
    else
      out<<"NO"<<endl;
  }
  return 0;
}
