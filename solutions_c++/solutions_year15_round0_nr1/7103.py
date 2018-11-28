#include<bits/stdc++.h>

using namespace std;

int CharToInt(char c){
  return c-'0';
}

int main(){
  int T , SMax, test_case = 0;
  string audience;
  cin>>T;
  while( T-- ){
    cin>>SMax>>audience;
    int standing_up = CharToInt(audience[0]) , ans = 0;
    for(int i=1; i<=SMax; ++i){
      if(i > standing_up){
        if(CharToInt(audience[i]) > 0){
          ans += i - standing_up;
          standing_up = i + CharToInt(audience[i]);
        }
      }
      else{
        standing_up += CharToInt(audience[i]);
      }
    }
    printf("Case #%d: %d\n",++test_case,ans);
  }
}
