//Esteban Foronda Sierra
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r;}
template <class T> long long toll(const T &x)
{ stringstream s; s << x; long long r; s >> r; return r;}

#define D(x) cout << #x " is " << x << endl
#define ll long long
#define MAXN 1000000

ll n;
int t, x = 1;
ll aux;
vector <int> g[MAXN];
ll d[MAXN];

string reverse(string a){
	string ans;
	for(int i = a.size() - 1; i >= 0; --i) ans += a[i];
	return ans;
}

void buildGraph(ll n){
	for(ll i = 0; i < n; ++i){
		string ns = reverse(toStr(i));
		if(toll(ns) <= MAXN){
			g[i].push_back(toll(ns));	
		}
		g[i].push_back(i + 1);
	}
}

void bfs(ll s){ // s = fuente, n = numero de nodos
	for (ll i = 0; i <= MAXN; ++i) d[i] = -1;
	queue <int> q;
	q.push(s);
	d[s] = 0;
	while (q.size() > 0){
		int cur = q.front();
		q.pop();
		for (int i = 0; i < g[cur].size(); ++i){
			int next = g[cur][i];
			if (d[next] == -1){
			d[next] = d[cur] + 1;
			q.push(next);
			}
		}
	}
}

int main(){
	cin >> t;
	buildGraph(MAXN);
	bfs(0);
	for(int x = 1; x <= t; ++x){
		cin >> n;
		printf("Case #%d: %lld\n", x, d[n]);
	}
	return 0;
}




