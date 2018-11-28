#include <cstdio>
#include <cstdlib>
int h[20];
bool ispal(long long k){
   long long tmp = k, cur = 0;
   while(k>0){
      h[cur] = k%10;
      k/=10;
      cur++;
   }
   for (int i = cur-1; i>=0; i--){
      if (tmp%10!=h[i]) return false;
      tmp/=10;
   }
   return true;
}
int a[1000];
int main(){
   int n, current = 0;
   for (long long i = 1; i!=10000000; i++){
      if (ispal(i) && ispal(i*i)) {
         a[current] = i*i;
         current++;
         //printf("%lld , %lld\n",i,  i*i);
      }
   }
   int T, A, B, sum, kl = 1;
   FILE *fi = fopen("first.in", "r");
   FILE *fo = fopen("out.out", "w");
   fscanf(fi, "%d", &T);
   while(T--){
      fscanf(fi, "%d%d", &A, &B);
      sum = 0;
      for (int i = 0; i<current; i++){
         if (a[i]>=A && a[i]<=B) sum++;
      }
      fprintf(fo, "Case #%d: %d\n", kl, sum);
      kl++;
   }
   system("pause");
}
