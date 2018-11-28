/*************************************************************************
Author: zjut_polym
Created Time:   2014/4/12 21:35:53
File Name: B.cpp
************************************************************************/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>
#include <queue>
using namespace std;


//----------------------[ZJUT-polym for div2]-------------------------------------
#define ll long long
#define MOD 1000000007
#define PII pair<int, int>
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define _mst(buf, val) memset(buf, val, sizeof(buf))
#define rep(i, l, r) for(i = (l); i <= (r); i++)
#define srep(i, l, r) for(i = (l); i >= (r); i--)
#define repi(it, c) for(typeof(c.begin())it = c.begin(); it != c.end(); it++)
#define inf 0x3f3f3f3f
#define N 100005
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------

int cnt[N];
bool vis[N];
int main() {
	int T, cas = 1, n, V;
	cin >> T;
	while(T--){
		printf("Case #%d: ", cas++);
		cin >> n >> V;
		for(int i = 0; i < n; i++){
			cin >> cnt[i];
//	cout << cnt[i] << endl;
		}
		sort(cnt, cnt + n);
		memset(vis, 0, sizeof(vis));
		int end = n - 1, ans = 0;
		for(int i = 0; i < n; i++){
			if(vis[i]) continue;
			vis[i] = true;
			while(end >= 0){
		//		cout << "end " << end << endl;
				if(vis[end]){end--;continue;}
				if(cnt[i] + cnt[end] > V) {end--; continue;}
				vis[end] = true; vis[i] = true; break;
			}
			//cout << i << " " << end << endl;
			ans++;
		}
		cout << ans << endl;
	}
    return 0;
}

