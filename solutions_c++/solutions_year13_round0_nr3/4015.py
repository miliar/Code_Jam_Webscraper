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

int a[10000005];
char s[20];

bool check(ll i){
    int l=0;
    while(i>0){
        s[l]=i%10;
        i/=10;
        l++;
    }
    for1(i,0,l/2)
       if(s[i]!=s[l-i-1]) return false;
    return true;
}

int main()
{
    int i,j,k,l,o,p;
    a[0]=0;
    for1(i,1,10000001)
       if(check(i)&& check(((ll)i)*i))
           a[i]=a[i-1]+1;
        else a[i]=a[i-1];
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    scanf("%d",&p);
    ll n,m;
    for1(o,1,p+1){
        cin>>n>>m;
        n=sqrt(n-1);
        m=sqrt(m);
        printf("Case #%d: %d\n",o,a[m]-a[n]);
    }
    return 0;
}
