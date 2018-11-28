#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  int n, j;
  cin >> n >> j;
  cout << "Case #1:" << endl;
  int ct = 0;
  char s[n + 1];
  for(int i = 1; i < n - 1; i++){
    s[i] = '0';
  }
  s[0] = '1';
  s[n - 1] = '1';
  s[n] = '\0';
  while(ct < j){
    int factors[11];
    char *pend;
    long int num;
    for(int b = 2; b <= 10; b++){
      factors[b] = -1;
    }
    for(int b = 2; b <= 10; b++){
      num = strtol(s, &pend, b);
      for(int p = 2; p <= (long int)sqrt(num); p++){
        if(num % p == 0){
          factors[b] = p;
          break;
        }
      }
    }
    int ok = 1;
    for(int b = 2; b <= 10; b++){
      if(factors[b] == -1){
        ok = 0;
        break;
      }
    }
    if(ok){
      ct++;
      cout << s << " ";
      for(int b = 2; b < 10; b++){
        cout << factors[b] << " ";
      }
      cout << factors[10] << endl;
    }
    long int newnum = strtol(s, &pend, 2);
    newnum += 2;
    for(int i = n - 1; i >= 0; i--){
      s[i] = '0' + newnum % 2;
      newnum = newnum / 2;
    }
  }
  return 0;
}