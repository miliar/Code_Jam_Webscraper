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
    double limit, extra, farm;
    double my;
    double income;
    double ans;
    double ans2;
    double t1,t2;
    double tacc;
    scanf("%d",&t);
    while (t--){
          scanf("%lf %lf %lf",&farm,&extra,&limit);
          ans = 0;
          ans2 = -1;
          income = 2;
          tacc = 0;
          int f = 0;
          printf("Case #%d: ",casos++);
          for (i=0;i<limit+100;++i){
              t1 = tacc + farm/income;
              t2 = tacc + limit/income;
              if (ans2 <= t2 && ans2 <= t1 && ans2!=-1){
                 printf("%.7lf\n",ans2); 
                 f=1;
                 break;
              }else if (t2 < t1){
                 if (ans2!=-1)
                     printf("%.7lf\n",min(ans2,t2));
                 else
                     printf("%.7lf\n",t2); 
                 f=1;  
                 break;
              } else {
                 if (ans2!=-1){
                    ans2 = min(ans2,t2);  
                 } 
                 else ans2 = t2;      
                 tacc = t1;
                 income += extra;    
              }
          }
          if(!f) printf("%.7lf\n",min(ans2,t2));   
    }
    
    
    return 0;
}




