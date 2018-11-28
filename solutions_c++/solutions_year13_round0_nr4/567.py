#include <iostream>
#include <algorithm>
#include <cstdio>
#include <utility>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string.h>
#include <cmath>
#define pii pai<int,int>
#define debug
using namespace std;

int dp[1<<26];
int abre[3000];
int qnt[3000];
int chaves[3000][3000];

int chaves_at[30000];
int chaves_init[202000];

int n,k;

int cont=0;

int get(long long bit){
    
 //   debug(" !! abre[1]=%d\n",abre[1]);
 //   debug("get %d (n=%d) (cont=%d)\n",bit,n,cont);
    
    if(dp[bit]+1)return dp[bit];
    cont++;
    
    
    
   // memset(chaves_at,0,sizeof(chaves_at));
    
   // for(int i=0;i<k;i++)chaves_at[chaves_init[i]]++;
   
    
    /*for(int i=0;i<n;i++){
            if(bit & (1<<i)){
                   
                    
                   chaves_at[abre[i]] = chaves_at[abre[i]] - 1;
                  
                   
                   for(int j=0;j<qnt[i];j++){
                           chaves_at[chaves[i][j]]++;            } 
                           
                   }
            }*/
   
    int u = 1;
    for(int i=0;i<n;i++){
            
            if(!(bit&(1<<i)))u=0;
            if(bit&(1<<i))continue;
          //  debug("i=%d abre_i = %d abre[1]=%d chavesat=%d\n",i,abre[i],abre[1],chaves_at[abre[i]]);
            if(chaves_at[abre[i]]==0)continue;
            assert(chaves_at[abre[i]]>0);
            
            chaves_at[abre[i]]--;
            for(int j=0;j<qnt[i];j++)
                    chaves_at[chaves[i][j]]++;
                    
            
            if(get(bit|(1<<i))+3)
                                  return dp[bit] = i;  
            chaves_at[abre[i]]++;
            for(int j=0;j<qnt[i];j++)
                    chaves_at[chaves[i][j]]--;  
                                 
                                     
            }
    if(u==1)return dp[bit] = -2;
    return dp[bit] = -3;
    
}

main(){
       
       int te;
       scanf("%d",&te);
       
       for(int t=1;t<=te;t++){
               
               memset(dp,-1,sizeof(dp));
               memset(chaves_at,0,sizeof(chaves_at));
               
               scanf("%d%d",&k,&n);
               
               for(int i=0;i<k;i++){
                       scanf("%d",chaves_init+i);
                       chaves_at[chaves_init[i]]++;
                       }
                      
               
               for(int i=0;i<n;i++){
                       
                       scanf("%d %d",abre+i,qnt+i);
                       
                       
                       for(int j=0;j<qnt[i];j++){
                               scanf("%d",&chaves[i][j]);
                               
                               }
                               
                       
                       
                       
                       }
              
               printf("Case #%d:",t);
               if(get(0)==-3)
                             printf(" IMPOSSIBLE\n");
               else{

                    long long bit = 0;
                    
                    while(get(bit)+2){
                                     
                                     printf(" %d",dp[bit]+1);
                                   
                                     bit |= (1<<get(bit));
                                     }
                    printf("\n");
                    
                    }
                       
               
               }
               }
