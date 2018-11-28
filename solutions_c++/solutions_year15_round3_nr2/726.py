/*

    Harsh Vardhan :)

*/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<iomanip>
#include<cstring>
#include<queue>
#include<stack>

using namespace std;

#define MAX 1111111
#define gi(n) scanf("%d",&n)
#define gl(n) scanf("%lld",&n)
#define pi(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define all(c) c.begin(), c.end()
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define tr(v, it) for(typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define mp make_pair
#define F first
#define S second
#define     inf             (0x7f7f7f7f)//>2e9
#define     For(i,a,b)      for(int i=a;i<=b;++i)
#define SET(p,v) memset(p, v, sizeof(p))
#define chkC(x,n) (x[n>>6]&(1<<((n>>1)&31)))
#define setC(x,n) (x[n>>6]|=(1<<((n>>1)&31)))
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
int K,TL,SL;
string keys;
string tword;
template<class T> T pwr(T b, T p){T r=1,x=b;while(p){if(p&1)r*=x;x*=x;p=(p>>1);}return r;}
pii sol(int idx,string s)
{
    if(idx==SL)
    {
        int ans = 0;
        For(i,0,SL-TL)
        {
            if(!s.compare(i,TL,tword))ans++;
        }
//        put(s," #end",ans);
        return mp(ans,ans);
    }
    pii ans = mp(0,-inf);
    For(i,0,K-1)
    {
        pii tmp = sol(idx+1,s+keys[i]);
        ans.S = max(ans.S,tmp.S);
        ans.F += tmp.F;
    }
    return ans;
}
int main()
{

	int t;
	gi(t);
	for(int i=1;i<=t;i++)
    {
        cin>>K>>TL>>SL;
        cin>>keys;
        cin>>tword;
        pii ans = sol(0,"");
        double ok = (double)ans.S-double(ans.F)/double(pwr(K,SL));
        cout<<"Case #"<<i<<": "<<setprecision(8)<<ok<<endl;

    }

     return 0;
 }