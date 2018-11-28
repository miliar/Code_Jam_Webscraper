#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
ll gcd(ll a, ll b){
	if (!b)
		return a;
	return gcd(b, a%b);
}
ll lcm(ll a, ll b){
	return b / gcd(a, b)*a;
}
#define FOR(I,N) for(int(i)=0;i<int(N);++i)
#define FORK(I,N,K) for(int(i)=0;i<int(N);i+=int(K))

int t, n;
ll calc(string &x){
	ll ret = 0;
	for (int i = 0; i < x.size(); ++i)
		ret = ret * 27 + x[i] - 'a' + 1;
	return ret;
}
vector<ll> Hash(string &x){
	vector<ll>ret;
	string str;
	for (int i = 0; i < x.size(); ++i){
		if (x[i] == ' ' && str.size()){
			ret.push_back(calc(str));
			str.clear();
		}
		else if (x[i] != ' ')
			str += x[i];
	}
	if (str.size())
		ret.push_back(calc(str));
	return ret;
}
int res;
multiset<int>a;
vector<ll>g[20];
int vis[30000];
void solve(int i){
	if (i == n){
		int c = 0;
		int l = -1;
		for (multiset<int>::iterator it = a.begin(); it != a.end(); ++it){
			if (*it == l)
				continue;
			l = *it;
			if (vis[*it]){
				++c;
				if (c == res)
					break;
			}
		}
		res = min(res, c);
		return;
	}
	for (int j = 0; j < g[i].size(); ++j)
		a.insert(g[i][j]);
	solve(i + 1);
	multiset<int>::iterator it;
	for (int j = 0; j < g[i].size(); ++j){
		it = a.find(g[i][j]);
		a.erase(it);
		++vis[g[i][j]];
	}
	solve(i + 1);
	for (int j = 0; j < g[i].size(); ++j)
		--vis[g[i][j]];
}
map<ll, int>mp;
int id;
int find(ll x){
	if (mp.find(x) == mp.end())
		return mp[x] = id++;
	return mp[x];
}
int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> n;
		string x, y;
		id = 0;
		mp.clear();
		getline(cin, x);
		getline(cin, x);
		getline(cin, y);
		memset(vis, 0, sizeof(vis));
		vector<ll> en = Hash(x);
		vector<ll> fr = Hash(y);
		sort(en.begin(), en.end());
		en.resize(unique(en.begin(), en.end()) - en.begin());
		sort(fr.begin(), fr.end());
		fr.resize(unique(fr.begin(), fr.end()) - fr.begin());
		a.clear(); 
		FOR(0, en.size())
			a.insert(find(en[i]));
		FOR(0, fr.size())
			vis[find(fr[i])] = 1;
		n -= 2;
		FOR(0, n){
			g[i].clear();
			getline(cin, x);
			g[i] = Hash(x);
			sort(g[i].begin(), g[i].end());
			g[i].resize(unique(g[i].begin(), g[i].end()) - g[i].begin());
			for (int j = 0; j < g[i].size(); ++j)
				g[i][j] = find(g[i][j]);
		}
		res = 1 << 20;
		solve(0);
		printf("Case #%d: %d\n", k, res);
	}
}