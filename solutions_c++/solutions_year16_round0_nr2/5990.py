#include <bits/stdc++.h>
using namespace std;

int num_of_case = 1;

void output(int v){
  cout << "Case #" << num_of_case++ << ": " << v << endl;
}

bool isAllUp(const string &s){
  for(int i=0; i < s.length(); i++){
    if(s[i] == '-') return false;
  }
  return true;
}

char flip(const char &c){
  if(c == '-') return '+';
  else return '-';
}

int main(void){
  int T; cin >> T;
  while(T--){
    string s; cin >> s;

    int ans = 0;
    while(1){
      for(int i = s.length() - 1; i >= 0; i--){
        if(s[i] == '-'){
          if(s[0] == '-'){
            for(int pos = 0; pos <= i; pos++){
              s[pos] = flip(s[pos]);
            }
            reverse(s.begin(), s.begin() + i + 1);
            ans++;
            break;
          }else{
            for(int j = i-1; j >= 0; j--){
              if(s[j] == '+'){
                for(int pos = 0; pos <= i; pos++){
                  s[pos] = flip(s[pos]);
                }
                reverse(s.begin(), s.begin() + j + 1);
                ans++;
                break;
              }
            }
            break;
          }
        }
      }
      if(isAllUp(s)) break;
    }
    output(ans);
  }
  return 0;
}
