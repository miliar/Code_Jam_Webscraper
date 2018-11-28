#include <bits/stdc++.h>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  int T, N,ans;
  freopen("A-large.in", "r", stdin);
  freopen("out", "w", stdout);
  scanf("%d", &T);
  for(int t = 1; t <= T; t++){
    //reads in everything
    scanf("%d", &N);
    if(N == 0){
        printf("Case #%d: %s", t, "INSOMNIA\n");
    }else{
       vector<char> v {'0','1','2','3','4','5','6','7','8','9'};
       string nStr;
       int index;
       for(int i = 1; !v.empty(); i++){
           ans = i*N;
           nStr = to_string(ans);
           for(int j = 0; j < nStr.length(); j++){
               char c = nStr[j];
               for(int k = 0; k < v.size(); k++){
                   if(c == v[k]){
                       v.erase(v.begin() + k);
                   }
               }
           }
       }
       printf("Case #%d: %d\n", t, ans);
    }

  }
  return 0;
}

