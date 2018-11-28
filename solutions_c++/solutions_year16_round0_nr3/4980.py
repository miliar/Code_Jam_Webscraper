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

long long int j3,ini,fin,p,a,b,c,d,e,f,g,h,i3;

long long int div(long long int val1)
{
long long int i;
for(i=2;i<sqrt(val1);i++)
{
if(val1%i==0)
return i;
}
return 0;
}

long long int check_base(long long int num,long long int base)
{
long long int j=0,val;
p=num;
val=0;
while(p!=0)
{
if(p%2)
{
val+=pow(base,j);
}
p=p/2;
j++;
}
return div(val);
}

int main()
{

int t;
s(t);
while(t--)
{
int n;
long long int i;
s(n);sll(j3);
ini=pow(2,n-1);
fin=pow(2,n)-1;
printf("Case #1:\n");
for(i=ini+1;i<=fin;i++)
{
if(i%2)
{
a=check_base(i,2);
b=check_base(i,3);
c=check_base(i,4);
d=check_base(i,5);
e=check_base(i,6);
f=check_base(i,7);
g=check_base(i,8);
h=check_base(i,9);
i3=check_base(i,10);
if(a!=0&&b!=0&&c!=0&&d!=0&&e!=0&&f!=0&&g!=0&&h!=0&&i3!=0)
{
string ans="";
p=i;
while(p!=0)
{
if(p%2)
{
ans='1'+ans;
}
else
ans='0'+ans;
p/=2;
}
cout<<ans<<" "<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<" "<<g<<" "<<h<<" "<<i3<<endl;
j3--;
}
if(j3==0)
break;
}
}
}
return 0;
}
