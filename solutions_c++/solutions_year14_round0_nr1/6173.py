#include <stdio.h>
#include <stdlib.h>
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
#define scan2(i,j) scanf(" %d %d",&i,&j)
#define scan3(i,j,k) scanf(" %d %d %d",&i,&j,&k)
#define print(i) printf("%d\n",i);
#define pb push_back 
#define sz(i) i.size()
#define reset(vec) memset(vec,0,sizeof(vec))
#define ord(vec) sort(vec.begin(),vec.end())
#define rev(vec) reverse(vec.begin(),vec.end())
#define MAX 35

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
    int t;
    int i,j,k, casos=1;
    int ans;
    scanf("%d",&t);
    int v1[4], v2[4];
    
    while (t--){
          scanf("%d",&ans);
          ans--;
          for (i=0;i<4;i++){
              for (j=0;j<4;j++){
                  if (i==ans){
                      scanf("%d",&v1[j]);
                  }else{
                      scanf("%*d");      
                  }    
              }    
          }
          scanf("%d",&ans);
          ans--;
          for (i=0;i<4;i++){
              for (j=0;j<4;j++){
                  if (i==ans){
                      scanf("%d",&v2[j]);
                  }else{
                      scanf("%*d");      
                  }    
              }    
          }
          int match = 0;
          int fans;
          for (i=0;i<4;i++){
              for (j=0;j<4;j++){
                  if (v1[i]==v2[j]){
                     match++;
                     fans = v1[i];
                     break;                  
                  }    
              }    
          }
          printf("Case #%d: ",casos++);
          if (match==1){
             printf("%d\n",fans);              
          }else if (match==0){
             printf("Volunteer cheated!\n");      
          }else{
             printf("Bad magician!\n");   
          }   
    }
    
    
    return 0;
}




