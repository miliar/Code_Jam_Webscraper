#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<bitset>
#include<unordered_map>
#include<unordered_set>
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
#define MOD 1000000007
#define N 2000
int n, m;
int bf[N];
int dis[N][N];
int p[N];
int main(){
	int T;
	scanf("%d", &T);
	FOE(cc,1,T){
		scanf("%d", &n);
		FOR(i,0,n) scanf("%d", bf + i);
		FOR(i,0,n) bf[i]--;
		int ans = 0;
		FOR(b,0,1 << n){
			m = 0;
			FOR(i,0,n) if ((1 << i) & b) p[m++] = i;
			if (ans >= m) continue;
			do{
				int ok = 1;
				FOR(i,0,m){
					int pv = (i - 1 + m) % m;
					int nx = (i + 1) % m;
					if (bf[p[i]] != p[pv] && bf[p[i]] != p[nx]){
						ok = 0;
						break;
					}
				}
				if (ok) ans = max(ans, m);
			}while(next_permutation(p, p + m));
		}
		printf("Case #%d: %d\n", cc, ans);
	}
	return 0;
}

