#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define MIn(a,b) a>b?b:a
#define MAx(a,b) a>b?a:b
#define S(n) scanf("%lld",&n)
#define P(n) printf("%d",n)
#define sl(n) scanf("%lld",&n)
#define mod 1000000007
#define ull unsigned long long
using namespace std;
int main()
{

    long long t,r,T,ans,count;
     freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    S(T);

    while(T--)
    {
        ans=0;
        count=-1;
        S(r);
        S(t);
        r=r+1;
        while(ans<=t)
        {
            ++count;
            ans+=((r+(2*count))*(r+(2*count)))-((r+(2*count)-1)*(r+(2*count)-1));

        }
        cout<<count<<endl;

    }
 return 0;
}
