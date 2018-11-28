#include <fstream>
#include <string>
#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in;
ofstream out;


int A,N;
vector<int> m;

void print() {
  cout<<">";
  for (int i=0;i<m.size();++i)
    cout<<" "<<m[i];
  cout<<endl;
}

int solve() {
  int moves = 0;
  int minsolve = m.size();
  int i;
  int a=A;
  sort(m.begin(),m.end());
  print();
  if (a<2) {
    return m.size();
  }
  for (i=0;i<m.size();) {
    if (i>0) assert(m[i]>=m[i-1]);
    if (a>m[i]) {
      cout << "eat "<< m[i]<< " A="<<a<<endl;
      a += m[i];
      ++i;
    } else {
      // add a-1
      a += a-1;
      moves ++;
    }
    int x = moves + m.size() - i;
    if (x < minsolve)
      minsolve = x;
  }
  return minsolve;
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
    cout<<"t="<<t<<endl;
    in >> A >> N;
    m.clear();
    for (int j=0;j<N;++j) {
      int x;
      in >> x;
      m.push_back(x);
    }
    out<<"Case #"<<t<<": "<<solve()<<endl;
  }
  return 0;
}
