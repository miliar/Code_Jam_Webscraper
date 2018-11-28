#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void reverse(string &str, int s, int e) {
  while(s<e) {
   char tmp = str[s];
   str[s] = str[e];
   str[e] = tmp;
   s++,e--;
  }
}

int main() {
  int N;
  cin >> N;
  for(int ii=0;ii<N;++ii) {
    string s;
    cin >> s;
    int flipCount  = 0;
    for(int i=s.length()-1;i>=0;--i) {
      if(s[i] == '+') continue;
      int k = 0;
      for(k=0;k<i;k++) if(s[k] == '-') break;
      if(k!=0) {
        for(int t=0;t<k;++t) s[t] = '-';
        flipCount++;
        reverse(s,0,k-1);
      }
      flipCount++;
      for(int k=0;k<=i;++k) {
        if(s[k] == '-') s[k] = '+';
        else s[k] = '-';
      }
      reverse(s,0,i);
    }
    cout << "Case #"<<ii+1<<": "<< flipCount<<"\n";
  }
  return 0;
}
