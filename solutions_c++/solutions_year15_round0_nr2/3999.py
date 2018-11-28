#include <cctype>
#include <climits>
#include <cmath>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <numeric>
#include <ratio>
#include <regex>
#include <string>
#include <tuple>
#include <utility>
#include <valarray>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#define INF ULLONG_MAX
#define MIN LLONG_MIN
#define pi 3.1415926535897932384626433832795

#define sz(v) v.size()
#define pb(x) push_back(x)
#define re return
#define sum(v) accumulate(v.begin(),v.end(),0)
#define asrt(v) sort(v.begin(),v.end())
#define dsrt(v) sort(v.rbegin(),v.rend())
#define rev(v) reverse(v.begin(),v.end())
#define str to_string
#define print(v) for (auto& i:v) cout<<i<<endl
#define print "Case #"+to_string(t1)+": " 

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;

int f(vi v) {
	if(v[0]<=3) re v[0];
	int x=v[0];
	if(sz(v)>x) re x;
	int m=9999;
	vi cpy1=v,cpy2=v;
	for(int i=0; i<sz(cpy1); i++) cpy1[i]-=1;
	for(int i=2; i<=x-2; i++) {
		v.clear();
		v=cpy2;
		if(i>x-i) break;
		v[0]=i;
		v.push_back(x-i);
		dsrt(v);
		m=min(m,1+f(v));
	}
	re min(m,1+f(cpy1));
}

int main() {
	freopen("Data/B.txt", "r", stdin);
	freopen("Data/B1.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1; t1<=T; t1++) {
		int D;
		cin>>D;
		vi v;
		for(int i=0; i<D; i++) {
			int x;
			cin>>x;
			v.push_back(x);
		}
		dsrt(v);
		int x=f(v);
		cout<<print<<x<<endl;
	}
	getchar();
	return 0;
}
