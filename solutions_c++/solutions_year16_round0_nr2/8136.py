#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define repm(i,a,b) for(int i=(a);i>(b);i--)
#define f(i,n) rep(i,0,n)
#define pn printf("\n")
#define ps printf(" ")
#define pi(n) printf("%d",n)
#define pis(n) printf("%d ",n)
#define pin(n) printf("%d\n",n)
#define si(n) scanf("%d",&n)
#define sii(m,n) scanf("%d %d",&m,&n)
#define siii(l,m,n) scanf("%d %d %d",&l,&m,&n)
#define pstr(str) printf("%s",str)
#define sstr(str) scanf("%s",str)
#define ff first
#define ss second
#define pb push_back 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<int>::iterator vii;
typedef pair<pair<ll,ll>,pair<ll,ll> > matrix;
#define mod 1000000007

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    si(t);
    f(q,t)
    {
        string s;
        cin>>s;
        int l=s.size(),k=0,del=0;
        f(i,l) if(s[i]!=s[k])
            {
                del++;
                k=i;
            }
        if(s[l-1]=='-') del++;
        printf("Case #%d: %d\n",q+1,del);
    }
    return 0;
}










































