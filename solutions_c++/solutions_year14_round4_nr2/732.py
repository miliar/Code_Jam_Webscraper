/*************************************************************************
Author: zjut_polym
CreMyplaceed Time:   2014/5/31 23:44:19
File Name: 
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
#define srep(i,n) for(i = 1;i <= n;i ++)
#define repi(it, c) for(typeof(c.begin())it = c.begin(); it != c.end(); it++)
#define inf 0x3f3f3f3f
#define N 2007
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------
int n;
int val[N];
int Myplace[N];
PII cnt[N];
int MOHB_ID[N];
void gao();
int main()
{
	int T, cas=1;
	cin>>T;
	while(T--) {
		printf("Case #%d: ",cas++);
		gao();
	}
	return 0;
}
void gao() {
	cin >> n;
	int i, j, l = 1, r = n, ans = 0;
	for(int i = 1; i <= n; i++){
		cin >> val[i];
		cnt[i] = PII(val[i],i);
	}
	sort(cnt + 1, cnt + n + 1);
	for(int i = 1; i <= n; i++){
		Myplace[i] = cnt[i].ss;
		MOHB_ID[Myplace[i]] = i;
	}
	for(int i = 1; i <= n; i++){
		int t1 = Myplace[i] - l, t2 = r - Myplace[i], z = Myplace[i], kk;
		if (t1 <= t2) {
			ans += t1;
			for(kk = z; kk > l; kk--) {
				swap(MOHB_ID[kk], MOHB_ID[kk-1]);
				swap(Myplace[MOHB_ID[kk]], Myplace[MOHB_ID[kk-1]]);
			}
			l++;
		}
		else {
			ans += t2;
			for(kk = z; kk < r; kk++) {
				swap(Myplace[MOHB_ID[kk]], Myplace[MOHB_ID[kk+1]]);
				swap(MOHB_ID[kk], MOHB_ID[kk+1]);
			}
			r--;
		}
	}
	cout << ans << endl;
}
