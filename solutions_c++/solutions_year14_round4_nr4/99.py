#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 1020304
#define MaxNode 1020304
#define MD 1000000007

int n,m;
int ans = 0, ansm = 0;
string s[111];
int lcp[111][111];
vector<int> V[111];
int p[111];
void dfs(int now) {
	if (now > n) {
		For(i,1,m) V[i].clear();
		For(i,1,n) V[p[i]].push_back(i);
		For(i,1,m) if (V[i].size() == 0) return ;
		int tans = 0;
		For(i,1,m) {
			++tans;
			For(j,1,V[i].size()) {
				tans += s[V[i][j - 1]].length();
				int maxlcp = 0;
				For(k,1,j - 1) maxlcp = max(maxlcp,lcp[V[i][k - 1]][V[i][j - 1]]);
				tans -= maxlcp;
			}
		}
		if (tans > ans) {
			ans = tans; ansm = 1;
		} else if (tans == ans) ++ansm;
		return ;
	}
	For(i,1,m) {
		p[now] = i;
		dfs(now + 1);
	}
}			
			
int main() {
	freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TTT,1,T) {
		printf("Case #%d: ",TTT);
		cin >> n >> m;
		For(i,1,n) cin >> s[i];
		For(i,1,n) For(j,1,n) {
			lcp[i][j] = min(s[i].length(),s[j].length());
			For(k,1,min(s[i].length(),s[j].length())) if (s[i][k - 1] != s[j][k - 1]) {
				lcp[i][j] = k - 1; break ;
			}
		}
		ans = 0, ansm = 0;
		dfs(1);
		cout << ans << ' ' << ansm << endl;
	}
	return 0;
}

