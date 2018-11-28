#define _CRT_SECURE_NO_WARNINGS
#include <numeric>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <sstream>

#pragma comment(linker, "/STACK:256000000")
using namespace std;
typedef long long ll;
template<typename T> int size(T &a) {return (int)a.size();}
template<typename T> T sqr(T a)  { return a * a; }

#define fi first
#define se second
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,a,b) for(int i=(a);i<(b); ++i)
#define REPD(i,a,b)for(int i=(b)-1;i>=a;--i)
#define _(a,b) memset((a), (b), sizeof(a))
#define all(a) a.begin(), a.end()
#define mp make_pair
#define pb push_back
#define ve vector


void solve() {
	int k,n;
	cin>>k>>n;
	ve<int> st(201);
	REP(i,0,k){
		int x;
		cin>>x;
		st[x]++;
	}
	ve<int> type(n);
	ve<ve<int> > inside(n);
	REP(i, 0, n) {
		cin>>type[i];
		int r;
		cin>>r;
		REP(iter,0,r) {
			int x;
			cin>>x;
			inside[i].pb(x);
		}
	}
	ve<int> d(1 << n, -1), pv(1 << n);
	queue<int> q;
	q.push(0);
	d[0]=1;
	while (size(q)) {
		int p=q.front();
		q.pop();
		if(p==(1<<n)-1) break;
		ve<int> cur = st;
		REP(i, 0, n) if (p & (1 << i)) {
			cur[type[i]] --;
			REP(v, 0, size(inside[i]))
				cur[inside[i][v]]++;
		}
		REP(to, 0, n) if (!(p & (1 << to))) {
			if (cur[type[to]]>0 && d[p ^ (1 << to)] == -1) {
				d[p ^ (1 << to)] = 1;
				pv[p ^ (1 << to)] = to;
				q.push(p ^ (1 << to));
			}
		}
	}
	if (d[(1 << n) - 1] == -1) {
		printf("IMPOSSIBLE");
	} else {
		ve<int> path ;
		for(int c = (1<<n)-1; c; c ^= 1 << pv[c])
			path.pb(pv[c]);
		reverse(all(path));
		REP(i,0,size(path))
			cout<<path[i]+1<<" ";
	}
	
}

int main() {
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	//ios_base::sync_with_stdio(false);
	
	
	int test;
	cin >> test;
	REP(t, 0, test) {
		printf("Case #%d: ", t+1);
		solve();
		printf("\n");
	}
	

#ifdef air
	//printf("\n\n%lf\n", clock() * 1e-3);
#endif

	return 0;
}