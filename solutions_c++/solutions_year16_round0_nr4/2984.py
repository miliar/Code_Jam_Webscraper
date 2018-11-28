#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <bitset>
#include <random>
#include <stack>
#include <list>
#include <unordered_set>
#include <ctime>
#include <unordered_map>

using namespace std;

#define ll long long
#define ld long double
#define sc second
#define fs first
#define mp make_pair

template<class T> T sqr(T x) { return x*x; }
ld pi = 3.1415926535897932384626433832795;

const int N = 3e5+10, l = 20;

int t;

ll pow(ll a, ll p){
	ll res = 1;
	for (int i = 0; i < p; i++)
		res *= a;
	return res;
}

void solve(int _case)
{
	ll k, c, s;
	cin >> k >> c >> s;
	vector<ll> ans;
	ll have_to = k;
	ll cur = min(2ll, k);
	while (cur <= pow(k, c)){
		ans.push_back(cur);
		cur += 1 + 2 * pow(k, c - 1);
	}
	cout << "Case #" << _case << ": ";// << ans << endl;
	if (s == k){
		for (int i = 1; i <= k; i++)
			cout << i << ' ';
		cout << endl;
		return;
	}
	if (ans.size() <= s && !(k > 1 && c < 2)){
		for (int i = 0; i < ans.size(); i++)
			cout << ans[i] << ' ';
		cout << endl;
	}
	else{
		cout << "IMPOSSIBLE" << endl;
	}
	return;
}


int main()
{
	FILE* f, *g;
	freopen_s(&f, "input.in", "r", stdin);
	freopen_s(&g, "output.txt", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++){
		solve(i + 1);
	}
	return 0;
}