//JAI KALI MAA - (JKM)..-----THERE IS NO SECRET INGREDIENT.
//www.moovon.me
#include<bits/stdc++.h>
/*#include<iostream>#include<vector>#include<algorithm>#include<string>#include<map>#include<set>#include<list>#include<bitset>#include<cmath>#include<cstdio>#include<ctimey>#include<cstdlib>#include<sstream>*/
using namespace std;
//template jkm
#define ll   long long
#define jkm()int t; scanf("%d",&t); while(t--)
#define vi   vector<int>
#define vs   vector<string>
#define mp(a,b)  make_pair(a,b)
#define pb(a)push_back(a)
#define sorta(v) sort(v.begin(), v.end())
#define sortd(v) sort(v.begin(), v.end(), greater<int>()) //here it is int...PLease change into required data type
#define si(n)scanf("%d",&n)
#define sll(n)   scanf("%lld",&n)
#define s2(a,b)  scanf("%lld%lld",&a,&b);
#define si2(a,b) scanf("%d%d",&a,&b);
#define s3(a,b,c)  scanf("%lld%lld%lld",&a,&b,&c);
#define s4(a,b,c,d)  scanf("%lld%lld%lld%lld",&a,&b,&c,&d);
#define ps   printf(" ")
#define pn   cout<<"\n";
#define id(n)scanf("%f",&n)
#define ss(n)scanf("%s",&n)
#define pi(n)printf("%d\n", n)
#define pll(n)   printf("%lld\n", n)
#define all(v)   v.begin(),v.end()
#define l(a) a.length()
#define sz(a)a.size()
#define M(x,i)   memset(x,i,sizeof(x))
#define rep(i,n)  for(int i=0;i<n;i++)
#define fr(i,a,b)for(int i=(a);i<=(b);i++)
#define frd(i,a,b)   for(int i=(a);i>=(b);i--)
#define debug(x) cout << '>' << #x << ':' << x << endl;
#define printarray(a,i,n)  for(int i=0; i<n; i++) cout<<a[i]<<" ";
#define ios {std::ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);}
#define inputarray()int n; cin>>n;int a[n]; rep(i,n) cin>>a[i];
 
 
template< class T > T gcd(T a, T b) {  while(b^=a^=b^=a%=b); return a; }  //gcd
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b);}  //lcm
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));} //bitcount
template<class T> inline bool isPrimeNumber(T n) {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T multiplyMod(T a,T b,T m) {return (T)((((ll)(a)*(ll)(b)%(ll)(m))+(ll)(m))%(ll)(m));}
template<class T> inline T powerMod(T p,int e,T m) {if(e==0)return 1%m;else if(e%2==0){T t=powerMod(p,e/2,m);return multiplyMod(t,t,m);}else return multiplyMod(powerMod(p,e-1,m),p,m);}
bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}
ll decimaltobinary(ll b) {ll p10 = 1, ret = 0;for(; b > 0; b >>= 1){ret += p10*(b&1);p10 *= 10;}return ret;}
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}
const double pi=acos(-1.0);
 
 
//__builtin_popcount(x);
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
//jkm template
/*inline void f(int &x) {
register int c = getchar_unlocked();
x = 0;
for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());
for(; c>47 && c<58 ; c = getchar_unlocked()) {
x = (x<<1) + (x<<3) + c - 48;
}
}*/
//freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
 
 
//----------------------------------------------CodeYard--------------------------------------------------//




int main(){
int z=0;
freopen("sunnyil.in","r",stdin);freopen("sunnyol.out","w",stdout);
jkm(){
string s;
int a[26];
for(int i=0;i<26;i++) a[i]=0;
cin>>s;
map<char,int> m;
for(int i=0;i<l(s);i++) {m[s[i]]++;}
string t="";

int x=m['Z'];
m['Z']-=x; m['E']-=x; m['R']-=x; m['O']-=x;
rep(i,x) t+='0';

x=m['W'];
m['T']-=x; m['W']-=x; m['O']-=x;
rep(i,x) t+='2';


x=m['U'];
m['F']-=x; m['O']-=x; m['U']-=x; m['R']-=x;
rep(i,x) t+='4';

x=m['X'];
m['S']-=x; m['I']-=x; m['X']-=x;
rep(i,x) t+='6';


x=m['G'];
m['E']-=x; m['I']-=x; m['G']-=x; m['H']-=x; m['T']-=x;
rep(i,x) t+='8';


x=m['O'];
m['O']-=x; m['N']-=x; m['E']-=x;
rep(i,x) t+='1';


x=m['H'];
m['T']-=x; m['H']-=x; m['R']-=x; m['E']-=x; m['E']-=x;
rep(i,x) t+='3';


x=m['S'];
m['S']-=x; m['E']-=x; m['V']-=x; m['E']-=x; m['N']-=x;
rep(i,x) t+='7';

x=m['F'];
m['F']-=x; m['I']-=x; m['V']-=x; m['E']-=x;
rep(i,x) t+='5';

x=m['I'];
rep(i,x) t+='9';

sort(all(t));
z++;
printf("Case #%d: ",z);
cout<<t;
pn;
}
}