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
#define FOB(i,n)        for(int i=n-1;i>=0;i--)
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
    string s;
    cin>>s;
    char pos='+';
    int ans=0;
    FOB(i,s.size())
    {
        if(s[i]!=pos)
            pos=s[i],ans++;
    }
    cout<<ans<<endl;
}
main()
{
    int t=getn();
    REP(i,t) {cout<<"Case #"<<i<<": ";test();}
}
