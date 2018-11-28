#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
#define debug 
char str[10001000];
int v[10010000];
long long ok[10001000];
long long n,k,qnt;

bool vog(char w){
     return w=='a'||w=='e'||w=='i'||w=='o'||w=='u';}
     
main(){
       
       int te;
       scanf("%d",&te);
       
       for(int t=1;t<=te;t++){
       
       qnt=0;
               
       scanf(" %s",str);
       scanf("%d",&k);
       
       n=strlen(str);
       assert(n < 1001000);
       int cons=0;
       
       for(int i=0;i<n;i++){
               if(vog(str[i]))cons=0;
               else cons++;
               if(cons >= k){
                       ok[qnt++] = i;
                       debug("ok: %d\n",i);
                       }
               }
               
      int ptr=0;
      long long ans=0;
      
      for(int i=0;i<n;i++){
              
              while(ok[ptr] < i+k-1 && ptr < qnt)ptr++;
              debug("i=%d ptr=%d\n",i,ptr);
              
              if(ptr==qnt)break;
              ans += n-ok[ptr];
              } 
               
               
               
               
               
       printf("Case #%d: %lld\n",t,ans);
               }
               }
