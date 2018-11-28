#include <cstdio>
#include <cstdlib>
#include <cstring>

#define MAXN 1005

using namespace std;

int main() {
   int T, Smax, ans;
   int S[MAXN];
   char shy[MAXN];
   int cum[MAXN];
   int diff;
   scanf("%d", &T);
for(int kase = 1; kase <= T; kase++) {
   memset(cum,(0),sizeof(cum));
   memset(S,(0),sizeof(S));
   ans = 0;
   scanf("%d %s", &Smax, shy);
   for(int i = 0; i <= Smax; i++)
      S[i] = shy[i]-'0';
   for(int i = 1; i <= Smax; i++)
      cum[i] = cum[i-1]+S[i-1];
   for(int i = 0; i <= Smax; i++) {
      if(cum[i] < i) {
         ans += i-cum[i];
         diff = i-cum[i];
         for(int j = i; j <= Smax; j++) {
            cum[j] += diff;
         }
      }
   }
   printf("Case #%d: %d\n", kase, ans);
}
   return 0;
}
