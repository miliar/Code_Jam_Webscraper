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
int n, m;
int T, a[100];
char s[100][100], t[100][100];
set<string> st[10];
int main(){
	scanf("%d", &T);
	FOE(cc,1,T){
		scanf("%d%d", &m, &n);
		FOR(i,0,m) scanf("%s", s[i]);
		FOR(i,0,m) a[i] = strlen(s[i]);
		FOR(i,0,m) FOR(j,0,a[i]) t[i][j] = s[i][a[i] - j - 1];
		FOR(i,0,m) t[i][a[i]] = 0;
		int mx = 0, cnt = 0;
		FOR(i,0,(1 << (2 * m))){
			FOR(j,0,4) st[j].clear();
			int ok = 1;
			FOR(j,0,m){
				int tmp = (i >> (2 * j)) & 3;
				//printf("%d ", tmp);
				if (tmp >= n){
					ok = 0;
					break;
				}
				FOE(k,0,a[j]) st[tmp].insert(&t[j][k]);
			}
			//puts("");
			if (!ok) continue;
			int tmp = 0;
			FOR(j,0,n) tmp += st[j].size();
			//printf("!!%d\n", tmp);
			if (tmp > mx){
				mx = tmp;
				cnt = 1;
			}
			else if (tmp == mx) cnt++;
		}
		printf("Case #%d: %d %d\n", cc, mx, cnt);
	}
	return 0;
}

