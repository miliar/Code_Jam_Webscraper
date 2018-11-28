#pragma comment(linker, "/STACK:36777216")
#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <ctime>

#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define vint vector<int>
#define rep(i,n) for (int i=0; i<n; i++)
#define ll long long

using namespace std;

const int INF=~(1<<31);
const double EPS=1;
const double PI=3.141592653589793;

bool palindrome(ll i) {
	vint dig;
	while(i) {
		dig.pb(i%10);
		i/=10;
	}
	rep(i,dig.sz/2) {
		if(dig[i]!=dig[dig.sz-i-1]) return 0;
	}
	return 1;
}

int main() {
#ifdef _DEBUG
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
#endif
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  vector<ll> ans;
  for(ll i=1; i<=10000000; i++) {
	  if (palindrome(i) && palindrome(i*i)) ans.pb(i*i);
  }
  int T;
  cin>>T;
  rep(t,T) {
	  ll a,b;
	  cin>>a>>b;
	  printf("Case #%d: %d\n",t+1,upper_bound(all(ans),b)-lower_bound(all(ans),a));
  }
  return 0;
}