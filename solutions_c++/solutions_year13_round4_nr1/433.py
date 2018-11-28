#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define base 1000002013ll
using namespace std;

LL calc(LL x, LL y, LL n){
	LL d = y - x;
	return (n * d - d * (d - 1) / 2) % base;
}

LL solve(){
	int n, m;
	scanf("%d%d", &n, &m);
	Mi M;
	int x, y, z;
	LL ans = 0;
	for (int i = 0; i < m; i++){
		scanf("%d%d%d", &x, &y, &z);
		if (M.find(x) == M.end())
			M[x] = z;
		else
			M[x] += z;
		if (M.find(y) == M.end())
			M[y] = -z;
		else
			M[y] -= z;
		ans = (ans + calc(x, y, n) * z) % base;
	}
	priority_queue< pair<int, int> > Q;
	for (MI ii = M.begin(); ii != M.end(); ii++){
		if (ii->second > 0)
			Q.push(*ii);
		if (ii->second < 0){
			int res = -ii->second;
			while (res > 0){
				if (Q.top().second <= res){
					ans = (ans - calc(Q.top().first, ii->first, n) * (LL)Q.top().second) % base;
					res -= Q.top().second;
					Q.pop();
				}
				else{
					ans = (ans - calc(Q.top().first, ii->first, n) * (LL)res) % base;
					pair<int, int> tmp = Q.top();
					tmp.second -= res;
					Q.pop(); Q.push(tmp);
					res = 0;
				}
			}
		}
	}
	return (ans + base) % base;
}

int main(){
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; i++)
		printf("Case #%d: %lld\n", i, solve());
	
	return 0;
}
