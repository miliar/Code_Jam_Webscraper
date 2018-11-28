// Does greedy work?
// Find the first - from the right.
// Find the first + from the left.
// Reverse to first +.
// Reverse to first -.
// Continue until done.
#include <vector>
#include <iostream>
#include <string>
using namespace std;



int min_flips(string x) {
  vector<int> Cm;
  vector<int> Cp;
  Cm.resize(x.size()+1);
  Cp.resize(x.size()+1);
  
  Cm[0]=0;
  Cp[0]=0;
  for (int i=0;i<x.size();i++) {
    if (x[i]=='-') {
      Cm[i+1]=Cm[i];
      Cp[i+1] = min(Cp[i]+2,Cm[i]+1);
    } else {
      Cp[i+1]=Cp[i];
      Cm[i+1]=min(Cm[i]+2,Cp[i]+1);
    }
  }
  return Cp[x.size()];
}
int main() {
  int I;
  cin >> I;
  string line;
  for (int i=1;i<=I;i++) {
    cin >> line;
    cout << "Case #"<<i<<": " << min_flips(line) << endl;
  }
}
