#include<cmath>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

#define sqr(a) (a)*(a)
#define cub(a) (a)*(a)*(a)
#define for1(i,a,b) for(i=(a);i<(b);i++)
#define for2(i,a,b) for(i=(a);i>(b);i--)
#define same(a) memset((a),0,sizeof(a));
#define ll long long

const int MOD = 1000000009;

int cmpint(const void*a,const void *b)
{
    if(((int*)a)[0]==((int*)b)[0])
      return ((int*)a)[1]-((int*)b)[1];
    return ((int*)a)[0]-((int*)b)[0];
}


int main()
{
    int o,p;
    ll i,j,n,m,k,l,t;
    ll ans1,ans2;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&p);
    for1(o,1,p+1){
        cin>>n>>m;
        l=1;
        ans1=0;
        for1(i,0,n) l*=2;
        n=l;
        k=m;
        l=n;
        ans2=n;
        t=2;
        if(k<l){
        while(k>l/2){
            ans1+=t;
            t*=2;
            k-=l/2;
            l/=2;
        }
        k=m;l=n;
        t=2;
        while(k<l){
            ans2=n-t;
            t*=2;
            l/=2;
        }
        }
        else {
            ans1=n-1;
            ans2=n-1;
        }


        printf("Case #%d: ",o);
        cout<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
