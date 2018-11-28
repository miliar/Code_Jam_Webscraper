#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main(void){
  int T, count;
  cin >> T;
  string s;
  char now;

  for(int i=1;i<=T;i++){
    cout << "Case #" << i << ": ";
    s = "";
    now = '-';
    count = 0;
    cin >> s;
    for(int j=s.size()-1;j>=0;j--){
      if(s[j] == now){
        count++;
        if(now == '+') now = '-';
        else now = '+';
      }
    }
    cout << count << endl;
  }

  return 0;
}
