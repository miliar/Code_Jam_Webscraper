#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main() {
   int T, X, R, C;
   scanf("%d\n", &T);
for(int kase = 1; kase <= T; kase++) {
   scanf("%d %d %d\n", &X, &R, &C);
   if(C > R) swap(R, C);
   bool ans = true;
   if((R*C)%X != 0) ans = false;
   if(X > R) ans = false;
   if(X == 3 and R == 3 and C == 1) ans = false;
   if(X == 4 and R == 4 and C == 1) ans = false;
   if(X == 4 and R == 4 and C == 2) ans = false;
   printf("Case #%d: %s\n", kase, ans ? "GABRIEL" : "RICHARD");
}
   return 0;
}
