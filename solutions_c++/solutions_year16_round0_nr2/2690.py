#include <iostream>
#include <fstream>
#include <string>
#define DN 1005
using namespace std;

string inp;
int T,bst[DN][2];

int main() {
  ifstream f("input.txt");
  ofstream g("output.txt");
  f>>T;
  for(int t=1; t<=T; ++t) {
    f>>inp;
    if(inp[0]=='+') {
      bst[0][1]=0;
      bst[0][0]=1;
    }else {
      bst[0][0]=0;
      bst[0][1]=1;
    }
    for(int i=1; i<inp.size(); ++i)
      if(inp[i]=='+') {
        bst[i][1]=bst[i-1][1];
        bst[i][0]=1+bst[i-1][1];
      }else {
        bst[i][0]=bst[i-1][0];
        bst[i][1]=1+bst[i-1][0];
      }

    g<<"Case #"<<t<<": "<<bst[inp.size()-1][1]<<'\n';
  }
}