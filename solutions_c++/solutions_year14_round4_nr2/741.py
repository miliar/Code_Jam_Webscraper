#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define LL long long
#define N 1010
int n, m;
int T;
int dp[N][N];
int a[N], b[N], c[N];
map<int, int> mp;
/*
int f(int x, int y){
	if (x >= n) return 0;
	if (dp[x][y] != -1) return dp[x][y];
	int t1 = dp[x][y] = f(x + 1, y + 1) + c[x] - y, t2 = f(x + 1, y) + (n - 1 - (x - y) - c[x]);
	printf("%d %d %d %d\n", x, y, t1, t2);
	return dp[x][y] = min(t1, t2);
}
*/
int main(){
	scanf("%d", &T);
	FOE(cc,1,T){
		mp.clear();
		scanf("%d", &n);
		FOR(i,0,n) scanf("%d", a + i);
		FOR(i,0,n) b[i] = a[i];
		sort(b, b + n);
		FOR(i,0,n) FOR(j,0,n) if (b[i] == a[j]) c[i] = j;
		FOR(i,0,n) mp[b[i]] = i;
		//FOR(i,0,n) printf("%d\n", c[i]);
		int t1 = 0, t2 = n - 1, ans = 0;
		FOR(i,0,n){
			if (c[i] - t1 < t2 - c[i]){
				while(c[i] > t1){
					swap(a[c[i]], a[c[i] - 1]);
					c[mp[a[c[i]]]]++;
					c[i]--;
					ans++;
				}
				t1++;
			}
			else{
				while(c[i] < t2){
					swap(a[c[i]], a[c[i] + 1]);
					c[mp[a[c[i]]]]--;
					c[i]++;
					ans++;
				}
				t2--;
			}
		}

		printf("Case #%d: %d\n", cc, ans);
	}
	return 0;
}

