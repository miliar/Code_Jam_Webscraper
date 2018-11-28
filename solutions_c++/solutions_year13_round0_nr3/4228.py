#include <cstring>
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define mp make_pair
#define ITER(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define mod 1000000007
#define MAXN 1000010
#define ff first
#define ss second
#define ll long long
#define get getchar//_unlocked
inline ll inp()
{
    ll n=0,s=1;
    char p=get();
    if(p=='-')
    s=-1;
    while((p<'0'||p>'9')&&p!=EOF)
    p=get();
    while(p>='0'&&p<='9')
    {
    n = (n<< 3) + (n<< 1) + (p - '0');
    p=get();
    };
    return n*s;
}
int check(ll n)
{
    int k,i;
    vector<ll>v;
    while(n)
    {
        k=n%10;
        v.pb(k);
        n=n/10;
    }
    for(i=0,k=v.size()-1;i<k;i++,k--)
    {
        if(v[i]!=v[k])
        return 0;
    }
    return 1;
}
ll a[100]={1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL};
int main()
{
    ll i,n,j,k,l,m,t,c=0,p;
    t=inp();
    for(p=1;p<=t;p++)
    {
        j=inp();k=inp();
        for(i=0,c=0;i<39;i++)
        {
            if(a[i]>=j&&a[i]<=k)
            c++;
        }
         printf("Case #%lld: %lld\n",p,c);
    }

    return 0;
}

