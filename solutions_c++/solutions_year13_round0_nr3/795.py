#include <iostream>
#include <algorithm>
#include <cstdio>
#include <utility>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#define pii pai<int,int>
#define debug
using namespace std;

long long v[10001000];
int qnt = 0;

int pal(long long x){
     
     long long  A = x;
     
     long long B = 0;
     
     while(x){
              B*=10;
              B += (x%10);
              x/=10;
              
              
              }
     return (A==B)?1:0;
     
     }

main(){
       
       int te;
       scanf("%d",&te);
       
       
       
       for(long long i=1;i<10001000;i++){
               
               if(pal(i) && pal(i*i))v[qnt++] =  i*i;
               
               }
       
       
       for(int t=1;t<=te;t++){
               
               
               long long a,b;
               scanf("%lld %lld",&a,&b);
               
               printf("Case #%d: %d\n",t,upper_bound(v,v+qnt,b) - upper_bound(v,v+qnt,a-1) );
               
               
               }}
