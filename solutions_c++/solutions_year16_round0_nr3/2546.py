/*
By Tianyi Chen. All rights reserved.
Date: 2016-04-09
*/
#include<bits/stdc++.h>
# 1 "/working/1460206282.cpp"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "/working/1460206282.cpp"
# 62 "/working/1460206282.cpp"
using namespace std;int n,j;__int128 one=1;vector<int>primes;int fact[1<<17];using bnt=__int128;inline bnt sqr_mod(bnt x,bnt n) {


__int128 t,y=x; x%=n; for (t=0;y;x=(x<<1)%n,y>>=1)
if (y&1)
t=(t+x)%n; return t;
}
inline bnt multi_mod(bnt x,bnt y,bnt n) {

bnt t; x%=n; for (t=0;y;x=(x<<1)%n,y>>=1)
if (y&1)
t=(t+x)%n; return t;}
inline bnt pow_mod(bnt a,bnt n,bnt m) {
bnt res=1; a%=m; while (n) {
if (n&1)res=multi_mod(res,a,m);  a=sqr_mod(a,m);  n>>=1; }
return res;}
namespace prime_test {
using bnt=__int128;
inline bool _witness(bnt a,bnt n,int t,bnt u) {
static bnt x0,x;  x0=pow_mod(a,u,n);  while (t--) {
x=sqr_mod(x0,n);   if (x==1&&x0!=1&&x0!=n-1)return true;   x0=x;  }
return x!=1; }
bool miller_rabin(bnt n) {
if (n<4)return 1;  if (!(n&1))return 0;  bnt __=n-1;int r=0;  while (!(__&1))__>>=1,++r;  static bnt a[]={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41};  if (binary_search(begin(a),end(a),n))return 1;  for (unsigned i=0;i<sizeof(a)/sizeof(bnt);++i) {
if (_witness(a[i],n,r,__))return false;  }
return true; }
inline bool go(bnt n) {
return miller_rabin(n); }
}
template<class T>
T gcd(T a,T b) {
return b?gcd(b,a%b):a;}
__int128 abs(__int128 i){return i<0?-i:i;}
namespace pollard_rho {
bnt get_factor(bnt n) {
if (prime_test::go(n))return 0;  if (n>2&&!(n&1))return 2;  if (n<1000) {
for (bnt i=3;i<n;i+=2)if (n%i==0)return i;   return 0;  }
bnt d,x=n-233,y=x;  int i=1,k=2;  while (true) {
++i;   x=(sqr_mod(x,n)+n-1)%n;
d=gcd(abs(y-x),n);   if (d!=1&&d!=n)return d;   if (i==k) { y=x;k<<=1; }
}
return 0; }
vector<bnt>ftp_rt; inline void _ftp(bnt n) {
if (prime_test::go(n)) { ftp_rt.push_back(n);return; }
bnt a=get_factor(n);  if (a) {
n/=a;   _ftp(a);_ftp(n);  } else ftp_rt.push_back(n); }
inline void ftp(bnt n) {
ftp_rt.clear();  _ftp(n); }
}
namespace prime_table {
const int limit=1<<17; bool isprime[limit]; void init() {
primes.reserve(limit/50);  memset(isprime,1,sizeof isprime);  for(int i=2;i<limit;++i)
if (isprime[i]) {
for (int j=i<<1;j<limit;j+=i)isprime[j]=0,fact[j]=i;    primes.push_back(i);   }
}
struct _init { _init() { init(); } }_init;}
inline __int128 getfact(__int128 i) {
if (i<prime_table::limit)return fact[i]; return pollard_rho::get_factor(i); return 0;}
namespace bf {
bool binrep[32]; inline __int128 ex(int base) {
__int128 rt=0;  for(int j=0;j<n;++j)
rt=rt*base+binrep[j];  return rt; }
void solve() {
long long divis[11];  __int128 limit=one<<n;  for (__int128 i=1|one<<(n-1);i<limit;i+=2) {
cerr<<(int64_t)i<<'\n';   for(int _=0;_<n;++_)binrep[_]=i>>_&1;   for(int base=2;base<=10;++base) {
if (!(divis[base]=getfact(ex(base))))goto nx;
}
for(int i=0;i<n;++i)putchar(binrep[i]+'0');   for(int i=2;i<=10;++i)printf(" %lld",divis[i]);   putchar('\n');   cerr<<j<<'\n';   if (--j==0)return;  nx:;  }
}
}
int main() {
freopen("C-large.out","w",stdout);  int _;scanf("%d",&_);puts("Case #1:"); scanf("%d%d",&n,&j); bf::solve();}