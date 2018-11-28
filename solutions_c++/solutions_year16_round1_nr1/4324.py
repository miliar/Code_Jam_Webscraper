#include <bits/stdc++.h>
#include<stdio.h>
#include<string.h>
using namespace std;

int main(){
  int T;
  
 // vector<char> iStr;
  freopen("A-large.in", "r", stdin);
  freopen("out", "w", stdout);
  
  scanf("%d", &T);
  
  for(int t = 1; t <= T; t++){
      char* iStr = new char[1001];
      scanf("%s", iStr);
      char* ans = new char[1001];
      ans[0] = iStr[0];
      for(int i = 1; iStr[i] != '\0'; i++){
          if(iStr[i] >= ans[0]){
             
              for(int j = i; j > 0; j--){
                  ans[j] = ans[j-1];
              }
              ans[0] = iStr[i];
          }else{
              ans[i] = iStr[i];
          }
      }
      printf("Case #%d: %s\n", t, ans);
  }
  return 0;
}