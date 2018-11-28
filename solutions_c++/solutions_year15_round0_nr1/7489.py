#include <bits/stdc++.h>
#include <fstream>

using namespace std;

#define LL_MAX 200000000000
#define MOD 1000000007
#define INF 1000000000
#define EPS 1e-14
#define PI 3.14159265358979

#define ll long long int
#define llu long long unsigned
#define ld long

#define mp make_pair
#define pb push_back
#define maX(a,b) ( (a) > (b) ? (a) : (b))
#define miN(a,b) ( (a) < (b) ? (a) : (b))
#define minelt(A) *min_element(b2e(A))
#define maxelt(A) *max_element(b2e(A))
#define s(a) scanf("%d",&a)
typedef vector<vector<int> > vvi;
typedef vector <ll> vi;
typedef pair <ll, ll> pii;
typedef pair <pii, ll> pii1;
typedef vector<bool> vb;
typedef vector<vector<bool> > vvb;
typedef vector<string> vs;
ll gcd(ll a, ll b) {if (a == 0 || b == 0) return max(a,b); if (b % a == 0) return a; return gcd(b%a, a);}
ll modpow(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
ll mulmod(ll a, ll b, ll m) {int64_t res = 0;while (a != 0){if(a & 1)res =(res+b)%m;a>>=1;b =(b<<1)%m;}return res;}
char buf[1<<20];
int main()
{
ifstream iffer;
ofstream myfile;
myfile.open ("output.out");
iffer.open("A-large.in");
int t,j,co,i,person,n;
iffer>>t;
j=0;
while(t--)
{
j++;
co=person=0;
iffer>>n;
char arr[n+1];
iffer>>arr;
person=arr[0]-'0';
for(i=1;i<strlen(arr);i++)
{
if(i>person)
{
co+=(i-person);
person+=(i-person);
}
person+=(arr[i]-'0');
}
myfile<<"Case #"<<j<<": "<<co<<endl;
}
iffer.close();
myfile.close();
return 0;
}
