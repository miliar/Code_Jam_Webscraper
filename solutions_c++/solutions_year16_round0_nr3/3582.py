#include <cstdio>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ll;
const int oo = 0x3f3f3f3f;
const ll maxn = 1e7 + 10;
const int S=20;
bool noprime[maxn];
int n, J;
int ss[555 + 1];

void init()
{
    cout << maxn << endl;
    memset(noprime, 0 , sizeof(noprime));
    noprime[0] = noprime[1] = 1;
    for(ll i = 2; i < maxn; ++i)
    {
        if(!noprime[i])
        {
            if(i > maxn / i) continue;
            for(ll j = i * i; j < maxn; j += i)
                noprime[j] = 1;
        }
    }

}
ll mult_mod(ll a,ll b,ll c)
{
    a%=c;
    b%=c;
    ll ret=0;
    while(b)
    {
        if(b&1)
        {
            ret+=a;
            ret%=c;
        }
        a<<=1;
        if(a>=c)a%=c;
        b>>=1;
    }
    return ret;
}

ll pow_mod(ll x,ll n,ll mod)//x^n%c
{
    if(n==1)return x%mod;
    x%=mod;
    ll tmp=x;
    ll ret=1;
    while(n)
    {
        if(n&1) ret=mult_mod(ret,tmp,mod);
        tmp=mult_mod(tmp,tmp,mod);
        n>>=1;
    }
    return ret;
}

bool check(ll a,ll n,ll x,ll t)
{
    ll ret=pow_mod(a,x,n);
    ll last=ret;
    for(int i=1; i<=t; i++)
    {
        ret=mult_mod(ret,ret,n);
        if(ret==1&&last!=1&&last!=n-1) return true;//合数
        last=ret;
    }
    if(ret!=1) return true;
    return false;
}

// Miller_Rabin()算法素数判定
//是素数返回true.(可能是伪素数，但概率极小)
//合数返回false;

bool ok(ll xx)
{
    if(xx<2)return false;
    if(xx==2)return true;
    if((xx&1)==0) return false;//偶数
    ll x=xx-1;
    ll t=0;
    while((x&1)==0)
    {
        x>>=1;
        t++;
    }
    for(int i=0; i<S; i++)
    {
        ll a=rand()%(xx-1)+1;//rand()需要stdlib.h头文件
        if(check(a,xx,x,t))
            return false;//合数
    }
    return true;
}

inline ll cal(int *x, int base)
{
    ll tmp = 1;
    ll sum = 0;
    for(int i = n; i >= 1; --i)
    {
        sum += tmp * x[i];
        tmp *= base;
    }
    return sum;
}
vector<ll> ans;
map<string, bool> mp;
ll print(ll x)
{
    for(ll i = 2 ; i * i <= x; ++i)
        if( x % i == 0) return i;
}
bool flag;
int cnt;
void dfs(int pos, int now)
{
    if(pos == 1) return;
    if(flag) return;
    ss[pos] = now;
	bool flag_ = 1;
	ll tmp;
	for(int i = 2; i <= 10 ; ++i)
	{
		tmp = cal(ss, i);
//		cout << tmp << endl;
		if(ok(tmp))
		{
			flag_ = 0;
			break;
		}
	}
	if(flag_)
	{
    	string ss_tmp;
        for(int i = 1; i <= n; ++i) ss_tmp += ss[i] + '0';
        if(mp[ss_tmp]) return;
        mp[ss_tmp] = 1;
        cout << ss_tmp << ' ';
        for(int j = 2; j <= 10 ; ++j) ans.push_back(cal(ss, j));
        int sz = ans.size();
        for(int k = 0; k < sz; ++k) printf("%lld%c",print(ans[k]), k == sz - 1 ? '\n' : ' ');
        ans.clear();
		if(++cnt >= J) flag = 1;
	}
	dfs(pos - 1, 0);
	dfs(pos - 1, 1);
}


int main()
{
//    init();
	freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    int T;
    int ca = 0;
    scanf("%d",&T);
    while(T--)
    {
    	mp.clear();
        scanf("%d %d",&n, &J);
        ss[1] = 1;
        ss[n] = 1;
        flag = 0;
        cnt = 0;
        for(int i = 2; i <= n - 1; ++i) ss[i] = 0;
        printf("Case #%d:\n",++ca);
//        for(int i = n - 1; i >= 2; --i)
//        {
            dfs(n - 1, 0);
            dfs(n - 1, 1);
//            dfs(i, 1, 2);
//            if(flag) break;
//        }
//		cout << cnt << endl;
    }
    return 0;
}
