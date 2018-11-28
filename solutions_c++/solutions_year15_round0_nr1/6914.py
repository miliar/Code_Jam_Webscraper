#include <iostream>
#include <string>
using namespace std;

int main() {
  int T=0, smax, a, p, members;
  string s;
  cin >> T;
  for(int i=1;i<=T;i++){
    a=0;
    p=0;
    cin >> smax;
    cin >> s;
    //cout << smax <<" "<< s << endl;
    p=s.at(0)-'0';
    for(int j=1; j<=smax; j++) {
      members = s.at(j)-'0';
      if(members>0){
        if(p>=j) {
          p+=s.at(j)-'0';
        } else{
          a+=j-p;
          p+=j-p+members;
        }
      }
    }
    cout << "Case #"<< i <<": "<< a << endl;
  }
  return 0;
}