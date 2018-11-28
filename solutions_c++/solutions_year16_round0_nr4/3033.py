#include <iostream>
#include <cmath>

using namespace std;

void fractiles_small(int ncase, int seqlen, int complexity, int s){
  cout << "Case #" << ncase << ":";
  for(int i=1;i<=s;++i){
    cout << " " << i;
  }
  cout << endl;
}

int main(){
  int ncases;
  cin >> ncases;
  for(int i=1;i<=ncases;++i){
    int seqlen, complexity, s;
    cin >> seqlen >> complexity >> s;
    fractiles_small(i, seqlen, complexity, s);
  }
  return 0;
}
