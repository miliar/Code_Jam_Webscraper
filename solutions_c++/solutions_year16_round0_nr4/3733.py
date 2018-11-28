#include<bits/stdc++.h>
#include<cmath>
#define ll long long int
#define P(n) printf("%lld",n)
#define Ps(n) printf("%s",n)
#define Pc(n) printf("%c",n)
#define PS() printf(" ")
#define Pn() printf("\n")
#define Sl(n) scanf("%lld",&n)
#define Si(n) scanf("%d",&n)
#define Sc(n) scanf("%c",&n)
#define Ss(n) scanf("%s",&n)
#define pb push_back
#define mp make_pair
#define pll pair< ll, ll >
#define repG(start,end,diff,var) for(var=start;var<end;var+=diff)
#define repL(start,end,diff,var) for(var=start;var>end;var-=diff)
#define TESTCASE ll t;Sl(t);while(t--)
#define mod (1000000000+7)
using namespace std;


ll i,j,k;
ll n,m,l,r,b,p;
string s,up,low;


int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("read.txt","w",stdout);
    int ti=1;
    TESTCASE{
        scanf("%lld%lld%lld",&r,&b,&p);
        printf("Case #%d: ",ti++);
        for(i=1;i<=p;i++){
            printf("%lld ",i);
        }
        printf("\n");
    }

    return 0;
}
