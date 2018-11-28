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

char str[1000];

int isPali(int x){
     sprintf(str,"%d",x);
     int i;
     int t=strlen(str);
     for (i=0;i<t && i<=(t/2);i++){
        if (str[i]!=str[(t-1)-i])
           return 0;    
     }
     return 1;    
}

int main(){
    int t,a,b,init,lim,x,i,casos=1;
    int ans;
    scan(t);
    
    while(t--){
       scan(a); scan(b);
       init = (int)sqrt(a);
       init-=2;
       if (init<0)
          init=0;
       lim = (int)sqrt(b);    
       lim+=3; 
       ans=0;     
       FOR(i,init,lim){       
          if (i==1){
             if (a>1)          
               continue;  
             ans++;
             continue;     
          }          
          if (isPali(i)){                      
             x=i*i;
             if (x<=b && x>=a && isPali(x)){
                ans++;            
             }
          }
       }
       printf("Case #%d: %d\n",casos++,ans);        
               
    }
    
    
    
    return 0;
}




