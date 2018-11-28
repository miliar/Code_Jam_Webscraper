#include <fstream>
#include <iostream>
#include <bitset>
#define LL long long
using namespace std;

int T,n;

int main() {
  ifstream f("input.txt");
  ofstream g("output.txt");
  f>>T;
  for(int t=1; t<=T; ++t) {
    f>>n;
    bitset<10> fol;
    int ok=0;
    for(int i=1; i<=100000; ++i) {
      LL cn=n*1LL*i;
      while(cn) {
        fol[cn%10]=1;
        cn/=10;
      }
      if(fol.count()==10) {
        g<<"Case #"<<t<<": "<<n*1LL*i<<'\n';
        ok=1;
        break;
      }
    }
    if(!ok) g<<"Case #"<<t<<": "<<"Insomnia\n";
  }
}