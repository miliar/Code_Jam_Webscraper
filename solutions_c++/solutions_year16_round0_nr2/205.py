#include <iostream>
#include <string>
using namespace std;
#define rep(var,n)  for(int var=0;var<(n);var++)

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
  	string s; cin >> s;

  	int L = s.size();
    char last = s[0];
    int sw = 0;
    for (int i=1; i<L; ++i) {
      if (s[i] != last) {
        ++sw;
        last = s[i];
      }
    }
    if (s[L-1] == '-') ++sw;

 answer:
    cout << "Case #" << (1+_t) << ": " << sw << endl;
  }
}
