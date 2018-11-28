#include <bits/stdc++.h>
using namespace std;

int _T;
string S;

int main(){
  scanf("%d", &_T);
  for(int _t = 1; _t <= _T; _t++){
    printf("Case #%d: ", _t);
    cin >> S;
    S.push_back('+');
    int res = 0;
    for(int i = 0; i + 1 < S.size(); i++){
      res += (S[i] != S[i + 1]);
    }
    printf("%d\n", res);
  }
}
