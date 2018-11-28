#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int t,smax;
string s;

int main() {
  ifstream f("input.txt");
  ofstream g("output.txt");
  f>>t;
  cout<<t;
  for(int T=1; T<=t; ++T) {
    f>>smax>>s; int pc=0,n=0;
    for(int i=0; i<=smax; ++i) {
      if(pc>=i) pc+=s[i]-'0';
      else {
        n+=i-pc;
        pc+=(i-pc);
        pc+=s[i]-'0';
      }
    }
    g<<"Case #"<<T<<": "<<n<<'\n';
  }
}