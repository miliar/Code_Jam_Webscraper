#include<iostream>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<string>
#include<cstring>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<bitset>
#include<cmath>

#define f(i,a,b) for(int i=a;i<b;i++)
#define b(i,a,b) for(int i=a;i>b;i--)
#define mpr(a,b) make_pair(a,b)
#define pr pair<int,int>
#define si(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define newline printf("\n")
#define ll long long 
using namespace std;
ll pwr(ll b,ll p)
{
    ll m=1;
    while(p!=0)
    {
        if(p%2==0)
        {
            b*=b;p/=2;
        }
        else 
        {
            m*=b;p--;
        }
    }
    return m;
}  
main()
{
    freopen("input1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    f(r,1,t+1)
    {
        ll k,c,s,a[102];
        cin>>k>>c>>s;
        f(i,1,s+1)
        a[i]=i;
        f(i,2,c+1)
        {
            f(j,1,s+1)
            {
                a[j]=(a[j]-1)*k+j;
            }
        }
        cout<<"Case #"<<r<<": ";
        f(i,1,s+1)
        cout<<a[i]<<" ";
        newline;
    }
}
        
