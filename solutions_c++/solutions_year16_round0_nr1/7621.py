#include <bits/stdc++.h>

using namespace std;

int get(long long n) {
   int ret = 0;
   while (n) {
      ret |= (1 << (n%10));
      n /= 10;
   }
   return ret;
}

int main() {
   
   int T;
   long long n;
   scanf("%d", &T);
   for(int qq=1; qq<=T; ++qq) {
      int mask = 0;
      scanf("%lld", &n);
      unordered_set<long long> st;
      mask |= get(n);
      st.insert(n);
      long long ans = -1, cc = n;
      for (int i=2; ; ++i) {
         if (mask == 1023) {
            ans = cc;
            break;
         } else {
            cc = n * i;
            if (st.find(cc) != st.end()) break;
            st.insert(cc);
            mask |= get(cc);
         }
      }
      if (ans == -1) printf("Case #%d: INSOMNIA\n", qq);
      else printf("Case #%d: %lld\n", qq, ans);
   }

   return 0;
}
