#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<complex>
#include<cstdlib>
#include<utility>

//structures
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<string>
using namespace std;
#define REP(i,n)        for(int i=1;i<=n;i++)
#define FOR(i,n)        for(int i=0;i<n;i++)
#define FOB(i,n)        for(int i=n;i>=1;i--)
#ifdef EBUG
#define DBG     if(1)
#else
#define DBG     if(0)
#endif
#define druha(x) ((x)*(x))
#define MP(x,y) make_pair((x),(y))
#define MT make_tuple
#define point complex<long double>
#define int long long
long long getn()
{
    long long h;
    scanf("%lld",&h);
    return h;
}
void test()
{
    int n=getn();
    if(n==0) {cout<<"INSOMNIA\n"; return;}
    vector<bool> bol(10);
    bool dalej=true;
    int k=0;
    while(dalej)
    {
        k++;
        int c=n*k;
        while(c)
        {
            bol[c%10]=1;
            c/=10;
        }
        dalej=false;
        FOR(i,10) if(!bol [i]) dalej=true;
    }
    cout<<n*k<<endl;
}
main()
{
    int t=getn();
    REP(i,t) {cout<<"Case #"<<i<<": ";test();}
}