#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>
#include<map>
#include<set>
#define Pi 3.14159265358
#define fi first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;
long long n, m, k, i, j, l, r, res, a[10000009];
int go(long long cur)
{
    int i;
    long long n;
    int cfr;
    bool bol;
    string s;
    bol=true;
    n=cur;
    cfr=0;
    while(n>0){
               cfr++;
               s+=n%10+'0';
               n/=10;
               }
    for(i=0;i<cfr/2;i++){
                         if(s[i]!=s[cfr-i-1]){
                                              bol=false;
                                              break;
                                              }          
                         }
    if(bol){
            return true;
            }
    return false;
}
int funct()
{
    long long i;
    a[1]=1;
    a[2]=4;
    a[3]=9;
    k=3;
    for(i=4;i<=10000000;i++){
                             if(go(i) && go(i*i)){
                                                  k++;
                                                  a[k]=i*i;
                                                  }
                             }
}
main(){
       freopen("codejamB.in","r",stdin);
       freopen("codejamB.out","w",stdout);
       funct();
       cin>>n;
       for(i=1;i<=n;i++){
                         res=0;
                         cin>>l;
                         cin>>r;
                         for(j=1;j<=k;j++){
                                           if(l<=a[j] && r>=a[j]){
                                                                  res++;
                                                                  }
                                           }
                         cout<<"Case #"<<i<<": "<<res;
                         cout<<endl;
                         }
       }
