#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;
typedef long long ll;
const ll maxn = 1e7;
const ll S = 20;

ll book[maxn] , cnt;

ll n , J;

vector<ll> p;

ll mod_mul(ll a, ll b, ll n) {
	ll res = 0;
	while(b) {
		if(b&1)    res = (res + a) % n;
		a = (a + a) % n;
		b >>= 1;
	}
	return res;
}
ll mod_exp(ll a, ll b, ll n) {
	ll res = 1;
	while(b) {
		if(b&1)    res = mod_mul(res, a, n);
		a = mod_mul(a, a, n);
		b >>= 1;
	}
	return res;
}
bool miller_rabin(ll n) {
	if(n == 2 || n == 3 || n == 5 || n == 7 || n == 11)    return true;
	if(n == 1 || !(n%2) || !(n%3) || !(n%5) || !(n%7) || !(n%11))    return false;

	ll x, pre, u;
	ll i, j, k = 0;
	u = n - 1;    //要求x^u % n

	while(!(u&1)) {    //如果u为偶数则u右移，用k记录移位数
		k++; u >>= 1;
	}

	srand((ll)time(0));
	for(i = 0; i < S; ++i) {    //进行S次测试
		x = rand()%(n-2) + 2;    //在[2, n)中取随机数
		if((x%n) == 0)    continue;

		x = mod_exp(x, u, n);    //先计算(x^u) % n，
		pre = x;
		for(j = 0; j < k; ++j) {    //把移位减掉的量补上，并在这地方加上二次探测
			x = mod_mul(x, x, n);
			if(x == 1 && pre != 1 && pre != n-1)    return false;    //二次探测定理，这里如果x = 1则pre 必须等于 1，或则 n-1否则可以判断不是素数
			pre = x;
		}
		if(x != 1)    return false;    //费马小定理
	}
	return true;
}

ll turn(string& s , ll base)
{
	ll b = 1 , now = 0;
	for(ll i=s.size()-1;i>=0;i--) now += (s[i]-'0')*b , b *= base;
	return now;
}

bool judge(string& s)
{
	vector<ll> v;
	for(ll i=2;i<=10;i++) 
	{
		ll now = turn(s, i);
		if(miller_rabin(now)) return false;
		bool ok = false;
		for(ll j=0;1LL*p[j]*p[j] <= now;j++) if(now % p[j] == 0) { v.push_back(p[j]); ok = true; break; }
		if(!ok) return false;
	}
	cout<<s<<"";
	for(ll i=0;i<v.size();i++) cout<<" "<<v[i]; cout<<endl;
	return true;
}

bool dfs(ll d , string s)
{
	if(d == n+1)
	{
		if(judge(s)) cnt++;
		return cnt == J;
	}
	
	s += '1';
	if(dfs(d+1, s)) return true;
	if(d == 1 || d == n) return false;
	s[s.size()-1] = '0';
	return dfs(d+1, s);
}

int main(int argc, char *argv[]) {
	freopen("out", "w", stdout);

for(ll i=2;i<maxn;i++)if(!book[i])
{
	p.push_back(i);
	for(ll j=i*2;j<maxn;j+=i) book[j] = 1;
}
	
	
	ll t;
	cin>>t;
	
	for(ll Case=1;Case<=t;Case++)
	{
		cin>>n>>J;
		
		cout<<"Case #"<<Case<<":\n";
		assert(dfs(1, ""));
	}
	
	return 0;
}