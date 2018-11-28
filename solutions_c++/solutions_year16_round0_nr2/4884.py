#include <iostream>
#include <string>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int t;
  string s;
  cin >> t;
  int ct = 0;
  for(int q = 0; q < t; q++){
    cin >> s;
    int l = s.length();
    for(int i = l - 1; i >= 0; i--){
      if(s[i] == '-'){
        for(int j = 0; j <= i; j++){
          s[j] = (s[j] == '-') ? '+' : '-';
        }
        ct++;
      }
    }
    cout << "Case #" << q + 1 << ": " << ct << endl;
    ct = 0;
  }
  return 0;
}