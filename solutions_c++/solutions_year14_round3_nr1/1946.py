#include <stdio.h>
#define LEN 50

long long checker[LEN];

void init(){
   long long mul = 1;
   for (long long i = 0; i < LEN; i++){
      checker[i] = mul;
      mul *= 2;
   }
}

bool check(long long A){
   for (int i = 0; i < LEN; i++){
      if (A == checker[i]) return true;
   }
   return false;
}

void swap(long long *A, long long *B){
   long long C;
   C = *A;
   *A = *B;
   *B = C;
}

long long GCD(long long A, long long B){
   if (A > B) swap(&A,&B);
   for (long long i = A; i >= A/2; i--){
      if (A%i == 0 && B%i == 0) return i;
   }
   return 1;
}

int main(){
   long long A,B,C,D,P,Q;
   int T;
   long long X;
   long long ans;
   
   //freopen("partelf.in","r",stdin);
   //freopen("partelf.out","w",stdout);
   
   init();
   scanf("%d",&T);
   
   for (int i = 0; i < T; i++){
      scanf("%lld/%lld",&P,&Q);
      X = GCD(P,Q);
      P /= X;
      Q /= X;
//      printf("%d. %lld/%lld\n",i+1,P,Q);
      if (Q%2 > 0) ans = -1;
      else if (!check(Q)) ans = -1;
      else{
         ans = 1;
//         /*
         while (P < Q/2){
            ans++;
            Q /= 2;
//            printf("%lld/%lld\n",P,Q);
         }
//         */
      }
      printf("Case #%d: ",i+1);
      if (ans == -1) printf("impossible\n");
      else printf("%lld\n",ans);
   }
   
   return 0;
}
