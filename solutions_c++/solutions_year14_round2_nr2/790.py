#include <sstream>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <string.h>
#include <assert.h>
#include <time.h>

#define LOCAL_TEST true
#define SZ(x) ((int)x.size())
#define all(a) a.begin(),a.end()
#define allr(a) a.rbegin(),a.rend()
#define clrall(name,val) memset(name,(val),sizeof(name));
#define clrint(name,val,s) memset(name,(val),sizeof(int)*s);
#define Assign(name,val) name.assign(val+1,vector<int>())
#define EPS 10e-6
#define ll long long
#define ull long long unsigned
#define SF scanf
#define PF printf
#define oo (1<<28)
#define psb(b) push_back((b))
#define ppb() pop_back()
#define mp make_pair
#define fs first
#define sc second
#define rep(var,s,n) for(var=(s);var<(n);(var)++)
#define rvp(var,s,n) for(var=(n-1);var>(s-1);(var)--)
#define read_ freopen("in.txt","r",stdin)
#define write_ freopen("out.txt","w",stdout)
#define __ std::ios_base::sync_with_stdio (false)

using namespace std;

ll DP[32][2][2][2];
int A,B,K;
ll rec(int pa,int fa,int fb,int fk)
{
    if(pa==-1)
    {
        return 1LL;
    }
    ll &ret = DP[pa][fa][fb][fk];
    if(ret!=-1) return ret;
    ret=0;
    int sa,ea;
    int sb,eb;
    int sk,ek;
    int nfa,nfb,nfk,b;
    sa=sb=sk=0;
    ea=(fa==0?((A>>pa)&1):1);
    eb=(fb==0?((B>>pa)&1):1);
    ek=(fk==0?((K>>pa)&1):1);
    for(int i=sa;i<=ea;i++)
    {
        if(fa==0&&i==ea) nfa=fa;
        else nfa=1;
        for(int j=sb;j<=eb;j++)
        {
            if(fb==0&&j==eb) nfb=fb;
            else nfb=1;
            b=(i&j);
            if(b>=sk&&b<=ek)
            {
                if(fk==0&&b==ek) nfk=fk;
                else nfk=1;
                ret+=rec(pa-1,nfa,nfb,nfk);
            }
        }
    }
    return ret;
}

int main()
{
    int cas=0,test,T;
    ll cnt;
    __;
    read_;
    write_;
    cin>>test;
    while(test--)
    {
        clrall(DP,-1);
        cin>>A>>B>>K;
        A--;
        B--;
        K--;
        cnt=rec(30,0,0,0);
        ++cas;
        cout<<"Case #"<<cas<<": "<<cnt<<endl;
    }
    return 0;
}





















