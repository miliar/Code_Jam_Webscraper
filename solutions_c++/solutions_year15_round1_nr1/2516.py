#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

bool feasible(int *M, int *m, int size) {
   for(int i = 0; i < size; i++)
      if(m[i] > M[i]) return false;
   return true;
}

int main() {
   int T, N, M[1100];
   int ans1, ans2;
   scanf("%d", &T);
for(int kase = 1; kase <= T; ++kase) {
   ans1 = ans2 = 0;
   scanf("%d", &N);
   for(int i = 0; i < N; ++i)
      scanf("%d", &M[i]);
   int maxima = -1;
   for(int i = 1; i < N; ++i) {
      if(M[i] < M[i-1]) ans1 += M[i-1]-M[i];
      maxima = max(maxima,M[i-1]-M[i]);
   }
   for(int i = 0; i < N-1; i++)
      if(M[i] > 0) ans2 += min(maxima,M[i]); 
   printf("Case #%d: %d %d\n", kase, ans1, ans2);
}
   return 0;
}
