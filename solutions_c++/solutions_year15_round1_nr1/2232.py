#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <limits.h>
#include <set>
using namespace std;

#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b) for(int (i) = (a); (i) < (b); ++(i))
#define rof(i,a,b) for(int (i) = (a); (i) > (b); --(i))
#define rep(i, c)  for(auto &(i) : (c))
#define x     first
#define y     second
#define pb  push_back
#define PB  pop_back()
#define iOS  ios_base::sync_with_stdio(false)
#define sqr(a)  (((a) * (a)))
#define all(a)  a.begin() , a.end()
#define error(x) cerr << #x << " = " << (x) << endl
#define Error(a,b) cerr << "( " << #a << " , " << #b <<" ) = ( " << (a) << " , " << (b) << " )\n";
#define errop(a) cerr << #a << " = ( " << ((a).x) << " , " << ((a).y) << " )\n";
#define coud(a,b) cout << fixed << setprecision((b)) << (a)
#define L(x)  ((x)<<1)
#define R(x)  (((x)<<1)+1)
#define umap  unordered_map
//#define max(x,y)  ((x) > (y) ? (x) : (y))
#define double long double
#define MOD 1000000007

int main() {
	int t; cin >> t;
	for (int z = 0; z < t; ++z)
	{
		int n, ans1 = 0, ans2 = 0, rate = 0; cin >> n;
		vector<int>v;
		for (int i = 0; i < n; ++i)
		{
			int dum; cin >> dum;
			v.push_back(dum);
		}
		for (int i = 0; i < n - 1; ++i)
		{
			if(v[i + 1] < v[i]) ans1 += v[i] - v[i + 1];
		}

		for (int i = 0; i < n - 1; ++i)
		{
			if(v[i] - v[i + 1] > rate) rate = v[i] - v[i + 1];
		}
		for (int i = 0; i < n - 1; ++i)
		{
			ans2 += min(v[i], rate);
		}
		cout << "Case #" << z + 1 << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}