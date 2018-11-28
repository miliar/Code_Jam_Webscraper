#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

#define MAXN 101

int T;
string s;
int pancakes[MAXN], N[MAXN], P[MAXN];

int main(){
  cin >> T;
  for(int cas=1; cas<=T; cas++){
    cin >> s;
    N[0] = P[0] = 0;
    for(int i=1; i<=s.length(); i++){
      N[i] = (s[i-1] == '-')? N[i-1] : P[i-1] + 1;
      P[i] = (s[i-1] == '+')? P[i-1] : N[i-1] + 1;
    }
    cout << "Case #" << cas << ": " << P[s.length()] << endl;
  }
  return 0;
}
