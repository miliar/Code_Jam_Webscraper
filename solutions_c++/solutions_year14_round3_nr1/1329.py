#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <climits>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9

using namespace std;

pair<ll,ll> p;
void fact(){
	ll a=p.f,b=p.s;
	while(true){
		ll x=__gcd(a,b);
		if(x==1)break;
		a/=x;b/=x;
	}
	p=mp(a,b);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		ll a,b;char tmp;
		cin>>a>>tmp>>b;
		p=mp(a,b);fact();a=p.f;b=p.s;
		int ans=0;
		bool check=false;
		while(b>a && b%2==0)b/=2,ans++;
		if(b!=1){
			while(b%2==0)b/=2;
			if(b!=1)check=true;
		}
		cout<<"Case #"<<++cs<<": ";
		if(check)cout<<"impossible\n";
		else cout<<ans<<"\n";
	}
	return 0;
}
