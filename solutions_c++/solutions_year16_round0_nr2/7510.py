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

string str,req;
map<string,int> mi;
string flip(int pos)
{
int i;
string temp1="";
for(i=pos;i>=0;i--)
temp1=temp1+((str[i]=='+')?'-':'+');
if(pos<str.length()-1)
{
for(i=pos+1;i<str.length();i++)
temp1=temp1+str[i];
}
return temp1;
}
int ans()
{
int ans1=0,i;
string temp;
queue<pair<string,int> > qu;
mi[str]=1;
if(str==req)
return 0;
qu.push(mp(str,0));
while(!qu.empty())
{
str=qu.front().first;
ans1=qu.front().second;
qu.pop();
for(i=0;i<str.length();i++)
{
temp=flip(i);
if(temp==req)
return ans1+1;
if(mi[temp]==0)
{
mi[temp]=1;
qu.push(mp(temp,ans1+1));
}
}
}
return ans1;
}
int main()
{
int t1,t,i;
s(t1);
for(t=1;t<=t1;t++)
{
mi.clear();
cin>>str;
req="";
for(i=0;i<str.length();i++)
req=req+'+';
printf("Case #%d: %d\n",t,ans());
}
return 0;
}

