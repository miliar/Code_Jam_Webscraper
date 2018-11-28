#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<map>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#define f(i,a,n) for(int i=a;i<n;i++)
#define ll long long
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define sd(a) scanf("%lf",&a)
#define ss(s) scanf("%s",s)
#define size 160000
using namespace std;
int main(){
freopen("dlarge.in","r",stdin);
freopen("dlarge.out","w",stdout);
int t;
si(t);
int x=0;
while(t--){
ll n;
sl(n);

vector< double >a,b,c,d;
double temp;
ll count=0,count1=0;
f(i,0,n){
sd(temp);          
a.push_back(temp);
c.push_back(temp);}

f(i,0,n){
sd(temp);          
b.push_back(temp);
d.push_back(temp);}

sort(a.begin(),a.end());
sort(b.begin(),b.end());
sort(c.begin(),c.end());
sort(d.begin(),d.end());

     f(i,0,n)
     f(j,0,n){         
     if(b[j]>a[i]){
     b[j]=-1.0;a[i]=-1.0; break ; 
     } }
    
     f(i,0,n)
     if(a[i]!=(-1.0) )
     count++;
     
     f(i,0,n)
     f(j,0,n){
      if(c[j]>d[i]){         
      count1++;
      c[j]=-1.0;d[i]=-1.0;break ; 
      }}        
     
    printf("Case #%d: %lld %lld\n",++x,count1,count);
    
}
return 0;
}
