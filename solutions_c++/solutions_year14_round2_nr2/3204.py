#include<cstdio>
int T,A,B,K,res=0;
int main(){
scanf("%d",&T);
for(int ii=1;ii<=T;ii++){
res=0;
scanf("%d",&A);
scanf("%d",&B);
scanf("%d",&K);
for(int i=0;i<A;i++){for(int j=0;j<B;j++)if((i&j)<K)res++;}
printf("Case #%d: %d\n",ii,res);
}
return 0;
}
