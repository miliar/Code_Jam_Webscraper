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
#define EPS 1e-9
#define ll long long
#define ull long long unsigned
#define SF scanf
#define PF printf
#define sf scanf
#define pf printf
#define psb(b) push_back((b))
#define ppb() pop_back()
#define oo (1<<28)
#define inf 0x3f3f3f3f
#define mp make_pair
#define mt make_tuple
#define get(a,b) get<b>(a)
#define fs first
#define sc second
#define Read freopen("CS.in","r",stdin)
#define Write freopen("CS.out","w",stdout)
#define __ std::ios_base::sync_with_stdio (false),cin.tie(0),cout.tie(0)

ll MulModL(ll B,ll P,ll M) {    ll R=0; while(P>0)      { if((P&1ll)==1) { R=(R+B); if(R>=M) R-=M; } P>>=1ll; B=(B+B); if(B>=M) B-=M; } return R; }

ll MulModD(ll B, ll P,ll M) {   ll I=((long double)B*(long double)P/(long double)M);    ll R=B*P-M*I; R=(R%M+M)%M;  return R; }

ll BigMod(ll B,ll P,ll M) {     ll R=1; while(P>0)      { if(P%2==1) { R=(R*B)%M; } P/=2; B=(B*B)%M; } return R; } /// (B^P)%M
ll power(ll B,ll P,ll M) {     ll R=1; while(P>0)      { if(P%2==1) { R=(R*B); } P/=2; B=(B*B); } return R; } /// (B^P)

template<class T1> void deb(T1 e1){cout<<e1<<"\n";}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<"\n";}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<"\n";}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<"\n";}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<"\n";}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<"\n";}
template<class T1,class T2,class T3,class T4,class T5,class T6,class T7> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6,T7 e7){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<" "<<e7<<"\n";}

//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//int dx[]= {0,0,1,-1};/*4 side move*/
//int dy[]= {-1,1,0,0};/*4 side move*/
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*night move*/

bool isPrime(ll n,vector<ll> &tmp)
{
    if(n%2==0)
    {
        tmp.psb(2);
        return false;
    }
    for(ll i=3;i<=n/i;i++)
    {
        if(n%i==0)
        {
            tmp.psb(i);
            return false;
        }
    }
    return true;
}

ll bin_to_num(int n)
{
    ll p=0;
    for(int i=15;i>-1;i--)
    {
        p=p*10ll+(ll)((n>>i)&1);
    }
    return p;
}

vector<vector<ll> > res;

bool isOK(int n)
{
    ll t,p;
    vector<ll> tmp;
    tmp.psb(bin_to_num(n));
    for(int i=2;i<11;i++)
    {
        t=0;
        p=1;
        for(int j=0;j<16;j++)
        {
            t=(ll)((n>>j)&1)*p+t;
            p*=(ll)i;
        }
        if(isPrime(t,tmp)) return false;
    }
    res.psb(tmp);
    return true;
}

int cnt=0;

void btk(int l,int n=0)
{
    if(cnt==50) return ;
    if(l==0)
    {
        if(isOK(n))
        {
            cnt++;
        }
        return ;
    }
    if(l==16||l==1) btk(l-1,(n<<1)|1);
    else
    {
        btk(l-1,(n<<1));
        btk(l-1,(n<<1)|1);
    }
    return ;
}

int main()
{
    #ifdef MAHDI
    Read;
    Write;
    #endif // MAHDI
    int t,n,k;
    cin>>t>>n>>k;
    btk(16);
    deb("Case #1:");
    for(int j=0;j<SZ(res);j++)
    {
        for(int i=0;i<SZ(res[j]);i++)
        {
            if(i) pf(" ");
            pf("%lld",res[j][i]);
        }
        pf("\n");
    }
    return 0;
}














