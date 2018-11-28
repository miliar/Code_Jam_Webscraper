//@ Including Header
// Name : ChouUn's Standard Library ֽũ�α�׼��
// Copyright : fateud.com
#ifndef CSL_STD_H_
#define CSL_STD_H_ 20151122L
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef std::pair<int,int> pii;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::vector<pii> vpii;

#define rep(i,a,b) for(auto i=a,i##_n=b;i<i##_n;++i)
#define rrep(i,a,b) for(auto i=b,i##_n=a;i-->i##_n;)

#endif /* CSL_STD_H_ */


/**
 *  Name : std.cpp
 *  Date : 2016��4��16�� ����8:59:57
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

#define N 1010
vi g[N], gg[N];
int v[N], w[N];
int ans, stamp = 1;
vpii h;

void dfs(int u, int f, int st, int ww) {
  if (v[u]) {
  	if (ww == w[u]) {
		ans = max(ans, st - v[u]);
	  	if (st - v[u] == 2) h.push_back(make_pair(u, f));  
	}
  	return;
  }
  v[u] = st, w[u] = ww;
  for(auto& v : g[u]) dfs(v, u, st + 1, ww);
}

int ma, cnt;
void search(int u, int f, int st) {
  if (v[u]) return; v[u] = true;
  if (st > ma) ma = st;
  for(auto& v : gg[u]) 
  	if (v != f) search(v, u, st + 1);
}
void count(int u, int f) {
  ma = 1;
  search(u, f, 1);
  cnt += ma;
  
  ma = 1;
  search(f, u, 1);
  cnt += ma;
}

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
	int n; cin >> n; 
	rep(i, 1, n+1) g[i].clear(), gg[i].clear();
	rep(i, 1, n+1) { int x; cin >> x; g[i].push_back(x); gg[x].push_back(i); }
	
	memset(v, 0x00, sizeof v);
	ans = 1, h.clear();
	rep(i, 1, n+1) if (!v[i]) dfs(i, 0, 1, stamp++);
	
  	memset(v, 0x00, sizeof v);
  	cnt = 0;
	for (auto& p : h) count(p.first, p.second);
	
	cout << max(cnt, ans) << endl;
  }
  return 0;
}

