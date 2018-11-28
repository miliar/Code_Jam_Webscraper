#include <bits/stdc++.h>

using namespace std;

string s;

int solve() {
   int len = s.length();
   int ret = 0;
   for (int i = len - 1; i >= 0; --i) {
      if (s[i] == '+') continue;
      s[i] = '+';
      ret ++;
      int j;
      for (j = i - 1; j >= 1; --j) {
         if (s[j] == '-') {
            s[j] = '+';
         } else break;
      }
      i = j;
      for (int z = i; z >= 0; --z) {
         s[z] = s[z] == '+' ? '-' : '+';
      }
      i ++;
   }
   return ret;
}

int main() {
   
   int T;
   scanf("%d", &T);
   for(int qq=1; qq<=T; ++qq) {
      cin >> s;
      printf("Case #%d: %d\n", qq, solve());
   }

   return 0;
}
