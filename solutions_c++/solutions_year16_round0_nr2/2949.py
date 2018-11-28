#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("my.in");
ofstream fout("my.out");

void foo(){
  string s;
  fin >> s;
  
  char last = s[0];
  int count = 1;

  for(int i=1; i<s.size(); i++){
    if(s[i]==last) continue;
    ++count;
    last = s[i];
  }

  int ret;
  if(s[0]=='+'){
    ret = count/2*2;
  }
  else{
    ret = (count-1)/2*2+1;
  }

  fout << ret;
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