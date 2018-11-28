#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <utility>
#include <set>
#include <map>
#include <bitset>
#include <iostream>
#include <ctype.h>

#define gc getchar  //unlocked linux
#define MOD 1000000007
#define INF numeric_limits<int>::max();
#define FOR(i,v,n) for(i=v;i<n;i++)
#define scan(i) scanf(" %d",&i)
#define print(i) printf("%d\n",i);
#define pb push_back 
#define sz(i) i.size()
#define reset(vec) memset(vec,0,sizeof(vec))
#define ord(vec) sort(vec.begin(),vec.end())
#define rev(vec) reverse(vec.begin(),vec.end())
#define MAX 155

using namespace std;

inline void scanint(int &x){
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int cmp_double(double a, double b, double eps = 1e-9){
    return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

int main(){
    int t,i,j,v,no,casos=1,n,m,k;
    int tab[MAX][MAX];
    scan(t);
    while(t--){
       scan(n); scan(m);
       FOR(i,0,n){
           FOR(j,0,m){
              scan(tab[i][j]);               
           }                   
       }  
       no=0;        
       FOR(i,0,n){
           FOR(j,0,m){
               v = tab[i][j];
               no=0;
               FOR(k,0,m){
                  if (tab[i][k]>v){
                      no++; 
                      break;                               
                  }           
               }
               FOR(k,0,n){
                  if (tab[k][j]>v){
                      no++;  
                      break;                              
                  }           
               }
               if (no>=2)
                  break;       
           }
           if (no>=2)
              break;
       }
       printf("Case #%d: ",casos++);
       if (no>=2)
          printf("NO\n");
       else
          printf("YES\n");
                     
               
    }
    
    
    
    return 0;
}




