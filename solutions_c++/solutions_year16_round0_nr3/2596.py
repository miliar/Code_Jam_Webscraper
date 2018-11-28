#include <algorithm>
#include <array>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstdint>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <stack>
#include <utility>
#include <sstream>
#include <vector>
#include <queue>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
 
typedef vector<int> vi;
typedef vector<long> vl;
typedef vector<ll> vll;
typedef vector<ull> vull;
typedef vector<vi> vvi; 
typedef vector<vl> vvl; 
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<char> vc;
 
typedef vector<int>::iterator vi_it;
typedef vector<long>::iterator vl_it;
typedef vector<ll>::iterator vll_it;
 
typedef set<int> si;
typedef set<long> sl;
typedef set<char> sc;
typedef set<int>::iterator si_it;
typedef set<long>::iterator sl_it;
typedef set<string> ss;
typedef set<char> sc;
 
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<pii>::iterator vpii_it;
typedef pair<long,long> pll;
typedef pair<int,string> pis;
typedef vector<pis> vpis;
typedef vector<pll> vpll;
typedef map<int,int> mii;
typedef map<string,string> mss;
typedef map<string,long> msl;
typedef map<string,int> msi;
typedef map<long,long> mll;
typedef vector<mll> vmll;
typedef map<char,int> mci;
typedef vector<mci> vmci;
typedef vector<msi> vmsi;
typedef map<char,long> mcl;
typedef pair<char,long> pcl;
typedef vector<pcl> vpcl;
 
#define sz(a) int((a).size()) 
#define sl(a) int((a).length()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rall(c) (c).rbegin(),(c).rend() 
#define tr(container, it) for (auto it = container.begin(); it != container.end(); it++) 
#define exist(c,x) ((c).find(x) != (c).end()) 
#define existv(c,x) (find(all(c),x) != (c).end())
#define loc(c,x) ((c).find(x) - (c).begin()) 
#define locv(c,x) (find(all(c),x) - (c).begin())
#define wl(x) (cout << (x) << endl)
#define w(x) (cout << (x))
#define r(x) (cin >> x);
#define r2(x,y) (cin >> x >> y);
#define FOR(i,a,b) for (auto i = (a); i < (b); i++)
#define RFOR(i,a,b) for (auto i = (a); i > (b); i--)
#define PP(x) tr(x,it) cout << it->first << " " << it->second << endl
#define mp(x,y) make_pair((x),(y))
#define fi first
#define se second
 
//const ll mod=1000000007;
//vll fact(200001);
//ll powmod(ll a,ll b) { ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res; }
//ll go(ll x, ll y) { return 1ll * fact[x+y] * powmod(1ll * fact[x] * fact[y], mod - 2) % mod; }
// target = (cond) ? true_case : false_case
//std::string::size_type i = t.find(s);
//if ((size_type i = s.find("144")) != string::npos) s.erase(i, 3);
// while ((i = s.find("144")) != string::npos) s.erase(i, 3);
//std::string binary = std::bitset<16>(1561561654).to_string(); //to binary
//std::string binary = std::bitset<8>(123).to_string(); //to binary
//unsigned long decimal = std::bitset<8>(binary).to_ulong();
//string::size_type sz; c=stol(a,&sz);
//bool is_b_exists_in_a(string a, string b){long x=0;FOR(i,(long)0,sz(a)) if (a[i] == b[x]) { x++; if (x==sz(b)) return true; }return false;}
//string::iterator low;
//bool is_palindrome(string s){long sl=s.length();  FOR(i,(long)0,sl/2) if (s[i] != s[sl-1-i]) return false;    return true;}
//lb = lower_bound(all(q),pll(it->first,0))-q.begin();

ll _sieve_size;
bitset<1000010> bs;
vi primes;
void sieve(ll upperbound)
{
	_sieve_size = upperbound + 1;
	bs.set();
	bs[0] = bs[1] = 0;
	for (ll i = 2; i <= _sieve_size; i++)
		if (bs[i])
		{
			for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
			primes.push_back((int)i);
		}
}

int conv(int num, int to)
{
int res=0;

	string s = std::bitset<32>(num).to_string();
	FOR(i,0,sz(s)) if (s[i]=='1') res+=(int)pow((double)to,sz(s)-1-i);
	return res;
}

int main() {
int t,n,j;
ll sx[9],sy[9];
int fc;
bool found;
int d[9];
int converted;

	FILE *in, *out;freopen_s(&in, "in.txt", "r", stdin);freopen_s(&out, "out.txt", "w", stdout);

	sieve(1000000);
	r(t);
	FOR(i,1,t+1)
	{
		r(n);r(j);
		FOR(u,2,11)
		{
			sx[u-2] = (ll) pow((double)u,min(16,(n-1)%16));
			sy[u-2] = (ll) pow((double)u,max(16,(n-1))-16);
		}
		cout << "Case #" << i << ":" << endl;
		for(int w=0;;w++)
		{
			fc=0;
			FOR(k,0,9)
			{
				found = false;
				converted=conv(w,k+2)*(k+2);
				FOR(t,0,sz(primes))
				{
					if (primes[t]>sx[k]) break;
					if (((sx[k]%primes[t])*(sy[k]%primes[t])+converted+1) % primes[t] == 0) { d[k] = primes[t]; found = true; fc++; break; }
				}
				if (!found) break;
			}
			if (fc==9)
			{
				string ba = std::bitset<32>(w).to_string();
				cout << "1" << ba.substr(sz(ba)+2-n,n-2) << "1 ";
				FOR(k,0,9) cout << d[k] << " ";
				cout << endl;
				j--;
			}
			if (j==0) break;
		}
	}

	return 0;
}