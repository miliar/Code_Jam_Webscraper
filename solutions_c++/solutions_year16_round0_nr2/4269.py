#include <iostream>
#include <fstream>
//#include <string>
using namespace std;

int foo(ifstream& fin,ofstream& fout){
  string s;
  fin>>s;

  int toTrim = 0;
  for(int i = s.length() - 1; i >= 0; i--) {
    if(s[i] != '+')  
      break;
    toTrim++;
  }

  if(toTrim == s.length()) {
    fout<<"0";
    return 0;
  }
  s = s.substr(0, s.length() - toTrim);


  char last = s[0];
  int ans = 1;
  for(int i = 1; i < s.length(); i++) {
    if(s[i] != last) {
      ans++;
      last = s[i];
    }
  }

  fout<<ans;
  return ans;

}

int main(){
  ofstream fout;
  ifstream fin;
  fin.open("B-large.in");
  fout.open("Bb.out");
  
  cout<<"open success\n";
  
  int T = 0;
  fin>>T;
  
  cout<<"input size success\n";
  
  for(int i=0;i<T;i++){
    fout<<"Case #"<<i+1<<": ";
    cout<<foo(fin,fout)<<endl;
    fout<<endl;
  }

}