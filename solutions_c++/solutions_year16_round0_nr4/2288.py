#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("D-small-attempt0.in");
ofstream fout("D-small-attempt0.out");

void foo(){
  int k, c, s;
  fin >> k >> c >> s;
  for(int i=1; i<=s; i++)
    fout << i << " ";
}
int main(){
  int T;
  fin >> T;
  for(int i=1; i<=T; i++){
    fout << "Case #" << i << ": ";
    foo();
    fout << endl;
  }
}