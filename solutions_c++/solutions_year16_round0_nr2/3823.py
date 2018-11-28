#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main () {

  ifstream fin("B-large.in");
  ofstream fout("B-large.out");

  int T;
  string str;

  fin>>T;

  for(int i=1; i<=T; i++){
    fin>>str;
    int len = 0, last_minus = 0;
    for(int j=0; j< str.length(); j++) {
      if(j==0 || str.at(j) != str.at(j-1)) {
        len++;

        if(str.at(j)== '-') {
          last_minus = len;
        }
      }
    }

    fout<<"Case #"<<i<<": "<<last_minus<<endl;
  }

  fin.close();
  fout.close();
  return 0;
}