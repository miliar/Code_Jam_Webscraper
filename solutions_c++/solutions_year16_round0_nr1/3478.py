#include <stdio.h>
int main(){
   FILE *f = fopen("out2.txt", "wt");
   int t,ii;
   scanf("%d",&t);
   for(ii=0;ii<t;ii++){
      long long k,imsi;
      int n,real_count;
      int check[10]={0};
      int i;
      scanf("%d",&n);
      k=n;
      while(1){
         imsi=k;
         real_count=0;
         while(1){
            check[imsi%10]=1;
            imsi/=10;
            if(imsi==0) break;
         }
         for(i=0;i<10;i++) real_count+=check[i];
         if(real_count==10 || n==0) break;
         k+=n;
      }
      if(n==0) fprintf(f,"Case #%d: INSOMNIA\n",ii+1);
      else fprintf(f,"Case #%d: %lld\n",ii+1,k);
   }
   fclose(f);
}