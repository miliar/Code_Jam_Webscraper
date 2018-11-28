#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define EACH(t,i,c) for(t::iterator i=(c).begin(); i!=(c).end(); ++i)
const double EPS = 1e-10;
const double PI  = acos(-1.0);

int kth(ll n,int k){
	for (int i = 0; i < k; i++)
	{
		n/=10;
	}
	return n%10;
}
int len(ll n){
	int ret=0;
	while(n){
		n/=10;
		ret++;
	}
	return ret;
}

bool palindrome(ll n){
	int l=len(n);
	for (int i = 0; i < l; i++)
	{
		if(kth(n,i)!=kth(n,l-i-1)){
			return false;
		}
	}
	return true;
}

int main() {
	int t;
	cin>>t;
	for (int test = 1; test <= t; test++)
	{
		ll a,b;
		cin>>a>>b;
		ll ans=0;
		for (ll i = ceil(sqrt(a)); i *i<=b ; i++)
		{
			if(palindrome(i)&&palindrome(i*i)){
				ans++;
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
}