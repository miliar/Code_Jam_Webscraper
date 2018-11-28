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
main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;ll n,m,p;
    si(t);
    f(i,1,t+1)
    {
        bool found[10]={false};int f=0,d;
        sll(n);m=n;p=n;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",i);
        else
        {
            while(f<10)
            {
                while(n!=0)
                {
                    d=n%10;
                    n=n/10;
                    if(found[d]==false)
                    {
                        f++;found[d]=true;
                    }
                }
                n=p+m;p=n;
                /*f(j,0,10)
                cout<<found[j]<<" ";cout<<n;newline;*/
            }
            n-=m;
            printf("Case #%d: %d\n",i,n);
        }
    }
}
        
