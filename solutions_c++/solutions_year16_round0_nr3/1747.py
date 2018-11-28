#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
 
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define _D(p) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p)<<std::endl;
#define _D2(p,q) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p) << ", " #q " = "<<(q)<<std::endl;
#define _DN(v) std::cout<<"L"<<__LINE__<<" : " #v " = ["; rep(i,(v).size()) {std::cout<<v[i]<<(i==v.size()-1?"":", ");}std::cout<<"]"<<std::endl;
#define _DNN(v) std::cout<<"L"<<__LINE__<<" : " #v " = [" << std::endl; rep(i,(v).size()) {std::cout<<"	[";rep(j,(v)[0].size()){std::cout<<v[i][j]<<(j==v[0].size()-1?"":", ");}std::cout<<"],"<<std::endl;}std::cout<<"]"<<std::endl;
 
using namespace std; 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

using namespace std;

long long mypow(ll a, ll x){
	ll ans = 1;
	for (int i = 0; i < x; ++i)
	{
		ans *=a;
	}
	return ans;
}

long long change(ll num, ll pbase, ll nbase){
	ll ans = 0;
	ll n = num;
	for (ll i = 0; ; ++i)
	{
		ll q = n % nbase;
		ans += q * mypow(pbase, i);
		n = (n - q)/nbase;
		if (n <= 0)
		{
			break;
		}
	}
	return ans;
}

ll dtob(ll num){
	ll a = 0;
	ll n = num;
	for (ll i = 0; ; ++i)
	{
		a += (n % 2) * mypow(10, i);
		n /= 2;
		if ( n <= 0)
		{
			break;
		}
	}
	return a;
}

ll frac(ll num){
	if (!(num % 2)){return 2;}
	for (ll i = 3; mypow(i, 2) <= num; i+=2)
	{
		if(num %i == 0){return i;}
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	ll test;
	cin >> test;
	ll n, J;
	cin >> n >> J;
	ll p = n - 2;
	std::vector<std::vector<ll>> v;
	cout << "Case #1:" << endl;
	for (ll i = 0; i < mypow(2, p); ++i)
	{
		ll t = (mypow(2, p) + i) * 2 + 1;
		//_D(t);
		ll q = dtob(t);
		//_D(q);
		bool f = true;
		std::vector<ll> v0;
		v0.push_back(q);
		for (int j = 2; j <= 10; ++j)
		{
			ll c = change(q, j, 10);
			ll fr = frac(c);
			v0.push_back(fr);
			if(!fr){f = false;break;}
		}
		if(!f){v0.clear(); continue;}
		v.push_back(v0);
		if(v.size() == J){break;}
	}
	for (int j = 0; j < v.size(); ++j)
	{
		for (int l = 0; l < v[j].size(); ++l)
		{
			cout << " " << v[j][l];
		}
		cout << endl;
	}
	return 0;
}