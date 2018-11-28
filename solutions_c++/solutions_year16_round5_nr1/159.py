#include <stdio.h>
#include <string.h>
#include <stack>

char s[1000001];
std::stack<char> stk;

int main(){
   int T, n, ans;
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      scanf("%s", s);
      n = strlen(s);
      while(!stk.empty()) stk.pop();
      for(int i=0; i<n; ++i){
         if(!stk.empty() && stk.top() == s[i])
            stk.pop();
         else
            stk.push(s[i]);
      }
      ans = n * 5;
      while(!stk.empty()){
         stk.pop();
         stk.pop();
         ans -= 5;
      }
      printf("Case #%d: %d\n", t, ans);
   }
   return 0;
}
