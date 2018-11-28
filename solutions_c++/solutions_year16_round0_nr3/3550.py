//ITNOA
#include<bits/stdc++.h> 

using namespace std;
 
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

#define int long long 
#define rep(i, s, e) for(int i = s; i < e; i ++)
#define X first
#define Y second

typedef long long ll;
typedef long double ld;

const int maxN = 2000*1000 + 5;
const int mod = 10429;
const int base = 701;
const int SQ = 500;
const int maxL = 20;

ll cng(int mask, int base)
{
    ll pw = 1, res = 0;
    rep(i,0,16)
    {
	if(mask >> i & 1)
	    res += pw;
	pw *= base;
    }
    return res;
}

vector<int> v;
bool is_prime(ll x)
{
//    cout << x << endl;
    for(ll i = 2; i * i <= x; i ++)
	if(x % i == 0) { v.push_back(i); return false; }
    return true;
}


void solve()
{
    int N,j; cin >> N >> j;
    cout << endl;
    
    rep(mask,0,(1<<15))
    {
	if(!(mask & 1)) continue;
	bool fl = 0;
	int smask = mask ^ (1 << 15);
	v.clear();
	rep(i,2,11)
	    if(is_prime(cng(smask, i)))
	    {
		fl = 1; break;
	    }
	if(fl) continue;

	cout << bitset<16>(smask) << ' ';
	rep(i,0,(int)v.size())
	    cout << v[i] << ' ';
	cout << endl;
	j --;
	if(j == 0) break;
    } 
}

int32_t main()
{
    ios::sync_with_stdio(0); cin.tie(0);
    int N; cin >> N;
    rep(i,1,N+1)
    {
	cout << "Case #" << i << ": ";
	solve();
    }
    return 0;    
}
