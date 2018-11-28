#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std; 


long long mod=1000002013;

int o[1005],e[1005],p[1005];
int n,m;

long long f(long long k,long long p){
     long long res=(k*n)%mod;
     long long r=((k*(k-1))/2)%mod;
     res=(res-r+mod)%mod;
     res=(res*p)%mod;
     return res;
    }


int solve(){
    long long optrail=0;
    long long optpas=0;
    
    scanf("%d %d",&n,&m);
    
    for (int i=0;i<m;i++) scanf("%d %d %d",&o[i],&e[i],&p[i]);
    
    for (int i=0;i<m;i++){
        long long k=e[i]-o[i];
        optrail=(optrail+f(k,p[i]))%mod;
        }
    vector< pair<int,pair<int,int> > > v;
    
    for (int i=0;i<m;i++){
        v.push_back(make_pair(o[i],make_pair(1,p[i])));
        v.push_back(make_pair(e[i],make_pair(2,p[i])));
        }  
    
    
    priority_queue< pair<int,int> > Q;      
    
    sort(v.begin(),v.end());
    for (int i=0;i<v.size();i++){
       // printf(" i %d \n",i);
        if (v[i].second.first==1) Q.push(make_pair(v[i].first,v[i].second.second));
        if (v[i].second.first==2){
           int num=v[i].second.second;
           //printf("%d\n",num);
           while (num>0){
                 pair<int,int> x=Q.top();
                 //printf(": %d\n",x.second);
                 Q.pop();
                 if (x.second<=num){
                     num=num-x.second;
                     long long k=v[i].first-x.first;
                     optpas=(optpas + f(k,x.second))%mod;               
                     } else {
                     Q.push(make_pair(x.first,x.second-num));
                     long long k=v[i].first-x.first;
                     optpas=(optpas + f(k,num))%mod;
                     num=0;       
                     }
                 }                 
           }
        }
    //printf("%I64d %I64d\n",optrail,optpas);    
    return (optrail-optpas+mod)%mod;    
    }


int main(){
    int T;
    scanf("%d",&T);
    for (int i=0;i<T;i++){
        printf("Case #%d: %d\n",i+1,solve());
        }
    return 0;
    }
