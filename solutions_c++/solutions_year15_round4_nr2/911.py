#include <stdio.h>

#define max(x, y) (x>y? (x) : (y))
#define min(x, y) (x<y? (x) : (y))

long long getInt(){
   char s[101];
   int dot = 0;
   long long ret = 0;
   scanf("%s", s);
   for(char* c=s; *c != '\0'; ++c){
      if(*c == '.') dot = 1;
      else{
         ret = ret*10 + *c - '0';
         if(dot) dot++;
      }
   }
   if(dot == 0) dot = 1;
   while(dot < 5){
      ret *= 10;
      dot++;
   }
   return ret;
}

int main(){
   int T;
   int n;
   long long V, X;
   long long v[101], c[101];
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      scanf("%d", &n);
      V = getInt();
      X = getInt();
      for(int i=0; i<n; ++i){
         v[i] = getInt();
         c[i] = getInt();
      }
      // printf("%d %d %d\n", X, c[0], c[1]);
      printf("Case #%d: ", t);
      if(n == 1){
         if(X == c[0]) printf("%.7f\n", (double)V/(double)v[0]);
         else printf("IMPOSSIBLE\n");
      }
      else{
         if(c[0] == c[1]){
            if(X == c[0]){
               printf("%.7f\n", (double)V/(double)(v[0]+v[1]));
            }
            else printf("IMPOSSIBLE\n");
         }
         else{
            if(X > max(c[0], c[1]) || X < min(c[0], c[1]))
               printf("IMPOSSIBLE\n");
            else if(X == c[0])
               printf("%.7f\n", (double)V/(double)v[0]);
            else if(X == c[1])
               printf("%.7f\n", (double)V/(double)v[1]);
            else{
               double v0 = (double)V*(double)(X-c[1])/(double)(c[0]-c[1]);
               double v1 = (double)V - v0;
               printf("%.7f\n", max(v0/(double)v[0], v1/(double)v[1]));
            }
         }
      }
   }

   return 0;
}
