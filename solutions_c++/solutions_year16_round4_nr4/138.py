#include <stdio.h>
#include <algorithm>

unsigned a[101], b[101];
bool occupied[101];

unsigned getBit(int n, char* s){
   unsigned ret = 0;
   for(int i=0; i<n; ++i){
      ret = (ret << 1) + (s[i] - '0');
   }
   return ret;
}

bool dfs(int now, int n, int* perm){
   if(now == n) return true;
   int id = perm[now];
   bool work = false;
   for(int i=0; i<n; ++i){
      if(((b[id] >> i) & 1) && !occupied[i]){
         occupied[i] = true;
         work = true;
         if(!dfs(now+1, n, perm)) return false;
         occupied[i] = false;
      }
   }
   if(!work) return false;
   return true;
}

bool simulate(int n, int* perm){
   for(int i=0; i<n; ++i)
      occupied[i] = false;
   return dfs(0, n, perm);
}

bool check(int n){
   int perm[4] = {0, 1, 2, 3};
   do{
      if(!simulate(n, perm)) return false;
   } while(std::next_permutation(perm, perm+n));
   return true;
}

int main(){
   int T, N, ans;
   char tmp[101];
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      printf("Case #%d: ", t);
      scanf("%d", &N);
      for(int i=0; i<N; ++i){
         scanf("%s", tmp);
         a[i] = getBit(N, tmp);
      }
      ans = N*N;
      for(unsigned s=0; s<(1<<(N*N)); ++s){
         // printf("[%u]", s);
         bool valid = true;
         for(int i=0; i<N; ++i){
            b[i] = (s>>(N*i)) & ((1<<N)-1);
            if((b[i] & a[i]) != a[i])
               valid = false;
         }
         if(!valid) continue;
         if(check(N)){
            int diff = 0;
            for(int i=0; i<N; ++i){
               unsigned x = a[i] ^ b[i];
               for(int j=0; j<N; ++j)
                  if((x >> j) & 1) diff += 1;
            }
            if(diff < ans){
               // for(int i=0; i<N; ++i) printf("%u ", b[i]);
               // printf("\n");
               ans = diff;
            }
         }
      }
      printf("%d\n", ans);
   }
   return 0;
}
