#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <tr1/unordered_map>
#include <windows.h>

using namespace std;
using namespace tr1;

#define ft first
#define sd second

typedef long long LL;
typedef unsigned int UI;

const int MAXN = 511111;
const int MOD = 1e9 + 7;
const double eps = 1e-6;
const LL MAXL = (LL)(0x7fffffffffffffff);
const int MAXI = 0x7fffffff;

void dfs(map<int, int> pck, int sum, int &ans){
	if(sum >= ans) return;
	if(pck.empty()) return;
	map<int, int>::reverse_iterator it = pck.rbegin();
	if(it->ft <= 3){
		ans = min(ans, sum + it->ft);
		return;
	}
	for(int i = it->ft / 2; i >= 1; i--){
		map<int, int> cpy = pck;
		cpy.erase(it->ft);
		cpy[i] += it->sd;
		cpy[it->ft - i] += it->sd;
		ans = min(ans, sum + it->sd + cpy.rbegin()->ft);
		dfs(cpy, sum + it->sd, ans);
	}
}

int main(){

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	

	int T;
	cin >> T;
	for(int cases = 1; cases <= T; cases++){
		int n, ans = 0;
		cin >> n;
		map<int, int> pck;
		for(int i = 0; i < n; i++){
			int a;
			cin >> a;
			ans = max(ans, a);
			pck[a]++;
		}
		dfs(pck, 0, ans);
		printf("Case #%d: %d\n", cases, ans);
	}
}
