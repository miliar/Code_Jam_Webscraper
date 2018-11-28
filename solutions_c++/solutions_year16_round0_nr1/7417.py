#include <bits/stdc++.h>
using namespace std;
#define vi vector < int >
#define pii pair < int , int >
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define foreach(it,v) for( __typeof((v).begin())it = (v).begin() ; it != (v).end() ; it++ )
#define ll long long
#define llu unsigned long long
#define MOD 1589540031
#define INF 0x3f3f3f3f
#define dbg(x) { cout<< #x << ": " << (x) << endl; }
#define dbg2(x,y) { cout<< #x << ": " << (x) << " , " << #y << ": " << (y) << endl; }
#define all(x) x.begin(),x.end()
#define mset(x,v) memset(x, v, sizeof(x))
#define sz(x) (int)x.size()
#define s(a) scanf("%d",&a)
#define sl(a) scanf("%ld",&a)
#define sll(a) scanf("%lld",&a)
#ifdef DEBUG
#define XYZ(x) printf(x)
#else
#define XYZ(x)
#endif // DEBUG
ll gcd(ll a, ll b) {if (a == 0 || b == 0) return max(a,b); if (b % a == 0) return a; return gcd(b%a, a);}
ll hcf(ll a, ll b) {if(b>a) return (hcf(b, a)); if(a%b==0) return b; return (hcf(b, a%b));}
ll modpow(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
ll mulmod(ll a, ll b, ll m) {int64_t res = 0;while (a != 0){if(a & 1)res =(res+b)%m;a>>=1;b =(b<<1)%m;}return res;}

set<int> st;
int has[10];
int main()
{
int q,t,n,j,p,i,t1,flag;
s(t1);
for(t=1;t<=t1;t++)
{
flag=0;
j=1;
s(n);
q=n;
st.clear();
memset(has,0,sizeof(has));
while(1)
{
if(st.count(q)!=0)
{
flag=1;
break;
}
else
{
st.insert(q);
p=q;
while(p>0)
{
has[p%10]=1;
p=p/10;
}
for(i=0;i<10;i++)
{
if(has[i]==0)
break;
}
if(i==10)
{
flag=2;
break;
}
else
{
j=j+1;
q=n*j;
}
}
}
if(flag==2)
printf("Case #%d: %d\n",t,q);
else
printf("Case #%d: INSOMNIA\n",t);
}
return 0;
}

