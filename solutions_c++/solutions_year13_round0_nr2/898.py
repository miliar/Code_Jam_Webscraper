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

int v[1010][1010];
int n,m;

bool ok (int a,int b){
     
     int ret = 1;
     
     for(int i=0;i<n;i++){
             if(v[i][b] > v[a][b])ret=0;
             
             }
     
     if(ret)return 1;
     ret = 1;
     
     for(int i=0;i<m;i++){
             if(v[a][i] > v[a][b])ret=0;
             
             }
             
             return ret;
     
     
     }

main(){
       
       int te;
       scanf("%d",&te);
       
       for(int t=1;t<=te;t++){
               
               
               scanf("%d%d",&n,&m);
               
               for(int i=0;i<n;i++){
                       for(int j=0;j<m;j++)
                               scanf("%d",&v[i][j]);}
                               
                       int resp = 1;
               for(int i=0;i<n;i++){
               for(int j=0;j<m;j++){
                       if(!ok(i,j)){resp=0;}
                       
                       }}
               
               printf("Case #%d: %s\n",t,resp?"YES":"NO");


               
               
               }}
