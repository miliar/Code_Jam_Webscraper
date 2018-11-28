#include<stdio.h>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<string>
#include<climits>
#include<bitset>
#include<set>
#include<functional>

using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;

#ifdef _WIN32
    #define gx getchar
    #define px putchar
    #define ps putchar(' ')
    #define pn putchar('\n')
    #define DEBUG 1
#else
    #define gx getchar_unlocked
    #define px putchar_unlocked
    #define ps putchar_unlocked(' ')
    #define pn putchar_unlocked('\n')
    #define DEBUG 0
#endif

//input
void scan(int &n)
{
    int sign = 1;
    n = 0;
    char c = gx();
    while( c < '0' || c > '9' )
    {
        if( c == '-' ) sign = -1;
        c = gx();
    }
    while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();  n = n * sign;
}
void lscan(ll &n)
{
    int sign = 1;
    n = 0;
    char c = gx();
    while( c < '0' || c > '9' )
    {
        if( c == '-' )
        sign = -1;
        c = gx();
    }
    while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();  n = n * (ll)(sign);
}
int sscan(char a[])
{
    char c = gx();
    while(c==' ' || c=='\n') c=gx();
    int i=0;
    while(c!='\n')a[i++] = c,c=gx();
    a[i]=0;
    return i;
}
int wscan(char a[])
{
    char c = gx();
    while(c==' ' || c=='\n') c=gx();
    int i=0;
    while(c!='\n' && c!=' ')a[i++] = c,c=gx();
    a[i]=0;
    return i;
}

//output
void print(int n)
{
    if(n<0)
    {
        n=-n;
        px('-');
    }
    int i=10;
    char o[10];
    do{o[--i] = (n%10) + '0'; n/=10;}while(n);
    do{px(o[i]);}while(++i<10);
}
void lprint(ll n)
{
    if(n<0LL)
    {
        n=-n;
        px('-');
    }
    int i=21;
    char o[21];
    do{o[--i] = (n%10LL) + '0'; n/=10LL;}while(n);
    do{px(o[i]);}while(++i<21);
}
void sprint(const char a[])
{
    const char *p=a;
    while(*p)px(*p++);
}


ll po(ll a, ll b, ll m)
{
	ll x=1,y=a;
	while(b > 0)
	{
		if(b%2 == 1)
		{
			x=(x*y);
			if(x>m) x%=m;
		}
		y = (y*y);
		if(y>m) y%=m;
		b /= 2;
	}
	return x;
}

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const ll MOD = 1000000007LL;
const int siz = 1000005;

int n,j,ct;
vector<string> ans;
vector< vector<ll> > ansv;

ll prime(ll a)
{
    ll s = (ll)sqrt(a),i;
    for(i=2;i<=s;i++)
    {
        if( !(a%i) ) return i;
    }
    return 0;
}

int check(string s)
{
    ll num,base,i,mul;
    vector<ll> v;
    for(base=2;base<11;base++)
    {
        mul = 1;
        num = 0;
        for(i=0;i<n;i++,mul*=base) if(s[i] == '1') num += mul;
        v.push_back( prime(num) );
    }
    for(i=0;i<9;i++) if(!v[i]) return 0;
    reverse(s.begin(),s.end());
    ans.push_back(s);
    ansv.push_back(v);
    return 1;
}

void rec(string s, int len)
{
    if(ct==50) return;
    if(len==(n-1))
    {
        s += '1';
        if(check(s)) ct++;
        return;
    }
    rec(s+'1',len+1);
    if(ct==50) return;
    rec(s+'0',len+1);
    return;
}

int main()
{
    n = 16;
    j = 50;
    ct = 0;
    int i,k;
    rec("1",1);
    cout << "Case #1:" << endl;
    for(i=0;i<50;i++)
    {
        cout << ans[i] << " ";
        for(k=0;k<8;k++) cout << ansv[i][k] << " ";
        cout << ansv[i][8];
        pn;
    }
    return 0;
}
