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
#include <utility>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <string.h>
#include <assert.h>
#include <time.h>

using namespace std;

#define SZ(x) ((int)x.size())
#define all(a) a.begin(),a.end()
#define allr(a) a.rbegin(),a.rend()
#define clrall(name,val) memset(name,(val),sizeof(name));
#define EPS 10e-9
#define ll long long
#define ull long long unsigned
#define SF scanf
#define PF printf
#define psb(b) push_back((b))
#define ppb() pop_back()
#define oo (1<<28)
#define mp make_pair
#define mt make_tuple
#define get(a,b) get<b>(a)
#define fs first
#define sc second
#define Read freopen("BL.in","r",stdin)
#define Write freopen("BL.out","w",stdout)
#define __ std::ios_base::sync_with_stdio (false)

ll BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

template<class T1> void deb(T1 e1){cout<<e1<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}

//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//int dx[]= {0,0,1,-1};/*4 side move*/
//int dy[]= {-1,1,0,0};/*4 side move*/
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*night move*/


int par[105];
double dp[105][105][105];
int dplen[105][105][105];
int vp[105][105][105];
int cnt[500];
int loop=0;

string pat;

void kmp()
{
    int n=SZ(pat);
    par[0]=0;
    int k=0;
    for(int i=1;i<n;i++)
    {
        while(k>0 && pat[i]!=pat[k]) k = par[k-1];
        if(pat[i]==pat[k]) k++;
        par[i]=k;
    }
    return ;
}

int S,L,K;

int reclen(int pos,int match,int occ)
{
    if(pos==S) return occ;
    int &ret = dplen[pos][match][occ];
    int &vet = vp[pos][match][occ];
    if(vet==loop) return ret;
    vet=loop;
    ret=0;
    for(int i='A';i<='Z';i++)
    {
        if(cnt[i])
        {
            int nmatch=match,nocc=occ;
            if(nmatch==L) nmatch=par[nmatch-1];
            while(nmatch>0 && pat[nmatch]!=i) nmatch=par[nmatch-1];
            if(pat[nmatch]==i) nmatch++;
            if(nmatch==L) nocc++;
            ret=max(ret,reclen(pos+1,nmatch,nocc));
        }
    }
    return ret;
}

int mxocc;

double rec(int pos,int match,int occ)
{
    if(pos==S)
    {
        return mxocc-occ;
    }
    double &ret = dp[pos][match][occ];
    int &vet = vp[pos][match][occ];
    if(vet==loop) return ret;
    vet=loop;
    ret=0.0;
    for(int i='A';i<='Z';i++)
    {
        if(cnt[i])
        {
            int nmatch=match,nocc=occ;
            if(nmatch==L) nmatch=par[nmatch-1];
            while(nmatch>0 && pat[nmatch]!=i) nmatch=par[nmatch-1];
            if(pat[nmatch]==i) nmatch++;
            if(nmatch==L) nocc++;
            ret+=rec(pos+1,nmatch,nocc)*(1.0/(K*1.0))*(1.0*cnt[i]);
        }
    }
    return ret;
}

int main()
{
    #ifdef MAHDI
    Read;
    Write;
    #endif // MAHDI
    int t,cas=0;
    __;
    cin>>t;
    while(t--)
    {
        string tmp;
        cin>>K>>L>>S;
        cin>>tmp>>pat;
        loop++;
        clrall(cnt,0);
        for(int i=0;i<K;i++)
        {
            cnt[tmp[i]]++;
        }
        kmp();
        int ans=reclen(0,0,0);
        double rans=0.0;
        if(ans)
        {
            mxocc=ans;
            loop++;
            rans=rec(0,0,0);
        }
        cout<<fixed<<"Case #"<<(++cas)<<": "<<setprecision(10)<<rans<<"\n";
    }
    return 0;
}














