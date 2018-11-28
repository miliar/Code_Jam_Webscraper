//#pragma comment(linker,"/STACK:102400000,102400000")
//#include <cstdio>
//#include <vector>
//#include <cmath>
//#include <queue>
//#include <set>
//#include <map>
//#include <cstring>
//#include <string>
//#include <iostream>
//#include <time.h>
//#include <algorithm>
//using namespace std;
//typedef pair<int, int> pii;
//#define INF 0x7fffffff 
//#define mod 1000000007
//#define ftmp 1000000000
//#define llu unsigned long long 
//#define ll long long
//#define maxn 1005
//#define pi acos(-1.0)
//#define dis(x0, y0, x1, y1) sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))
//ll gcd(ll n, ll m){ return m ? gcd(m, n%m) : n; }
////struct node{int x, y;}b[maxn];
////bool comp(node a, node b){ return (a.x < b.x || a.x == b.x&&a.y < b.y); }
//int n, m, k, ans, y, s;
//char str[maxn];
//double a[maxn][maxn];
//double t,p,dans;
//int w[maxn],x[maxn];
//struct node{
//	double v;
//	int c;
//}dp[maxn][129][11];
//int main(){
//	while (scanf("%d%d",&n,&m)&&n){
//		int flag = 1;
//		for (int i = 1; i <= n; i++){
//			scanf("%lf%lf%lf%lf%lf%d", &a[i][0], &a[i][1], &a[i][2], &a[i][3], &x[i], &w[i]);
//		}
//		p = m;
//		dp[0][m][0].x = 0;
//		for (int i = 1; i <= n; i++){
//			for (int j = 100; j >= 0; j--){
//				dp[i][j][ma] = min(dp[i][j][ma], dp[i - 1][j][ma] + t);
//				for (int k = 0; k <= ma+w[i]; k++){
//					dp[i][j + x[i]][ma] = min(dp[i][j + x[i]][ma], dp[i][j][ma]);
//					dp[i][j << k][ma - k] = min(dp[i][j << k][ma - k], dp[i][j][ma]);
//				}
//			}
//		}
//		dans = INF;
//		for (int i = 0; i <= 100; i++)
//			for (int j = 0; j <= 10; j++)dans = min(dans, dp[n][i][j]);
//		if (flag)printf("%.2lf\n", dans);
//		else printf("Impossible\n");
//	}
//	return 0;
//}
//
//#pragma comment(linker,"/STACK:102400000,102400000")
//#include <cstdio>
//#include <vector>
//#include <cmath>
//#include <queue>
//#include <set>
//#include <map>
//#include <cstring>
//#include <string>
//#include <iostream>
//#include <time.h>
//#include <algorithm>
//using namespace std;
//typedef pair<int, int> pii;
//#define INF 0x7fffffff 
//#define mod 1000000007
//#define ftmp 1000000000
//#define llu unsigned long long 
//#define ll long long
//#define maxn 1005
//int n, m, ans;
//int a[maxn], b[maxn], c[maxn];
//void bfs(int u){
//	queue<int>q;
//	q.push(u);
//	while (!q.empty()){
//		int u = q.front(); q.pop();
//		for (int i = 0; i < n; i++){
//
//		}
//	}
//}
//int main(){
//	while (~scanf("%d", &n)){
//		for (int i = 0; i < n; i++){
//			scanf("%d%d%d", &a[i], &b[i], &c[i]);
//		}
//		bfs();
//		if (ans)printf("NO\n");
//		else printf("%d\n", ans);
//	}
//	return 0;
//}

//#include <cstdio>
//#include <cstring>
//using namespace std;
//#define maxn 100067
//int t, n, m;
//char str[maxn];
//int a[maxn];
//int main(){
//	scanf("%d", &t);
//	while (t--){
//		memset(a, 0, sizeof a);
//		scanf("%s", str);
//		n = strlen(str);
//		for (int i = 0; i < n; i++){
//			if (str[i] == '(')a[i] = -1;
//			if (str[i] == '[')a[i] = -2;
//			if (str[i] == ')')a[i] = 1;
//			if (str[i] == ']')a[i] = 2;
//		}
//		int s = 0;
//		for (int i = 0; i < n; i++){
//			int x = 0, ma = 0, p = 0,k=-1;
//			for (int i = 0; i < n-1; i++){
//				if (a[i] == -1 && a[i + 1] == 1 || a[i] == -2 && a[i + 1] == 2)a[i] = 0, a[i + 1] = 0,p++;
//			}
//			if (p != 0)continue;
//			p = 0;
//			for (int i = 0; i < n; i++)if (a[i] == 0)p++;
//			if (p == n)break;
//			for (int i = 0; i<n;i++){
//				if (a[i]<0)x++;
//				if (a[i]>0)x--;
//				if (x >ma)ma = x, k = i;
//			}
//			if(k!=-1)a[k] = 0, s++;
//		}
//		printf("%d\n", s);
//	}
//	return 0;
//}
//
//



#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define maxn 1005
double a[maxn],b[maxn];
int vis[maxn];
int n, m, t, ans1,ans2;
void dfs1(int u,int k,int s){
	if (k == n){ ans1 = max(ans1, s); return; }
	for (int i = 0; i < n; i++){
		if (!vis[i]){
			vis[i] = 1;
			if (a[i] > b[k])s++;
			dfs1(i,k+1,s);
			if (a[i] > b[k])s--;
			vis[i] = 0;
		}
	}
}
void dfs2(int u, int k, int s){
	if (k == n){ ans2 = min(ans2, s); return; }
	for (int i = 0; i < n; i++){
		if (!vis[i]){
			vis[i] = 1;
			if (a[i] > b[k])s++;
			dfs2(i, k + 1, s);
			if (a[i] > b[k])s--;
			vis[i] = 0;
		}
	}
}
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas = 1;
	scanf("%d", &t);
	while (t--){
		memset(vis, 0, sizeof vis);
		ans1 = 0;
		ans2 = 10000;
		scanf("%d", &n);
		for (int i = 0; i < n; i++){
			scanf("%lf", &a[i]);
		}
		for (int i = 0; i < n; i++){
			scanf("%lf", &b[i]);
		}
		dfs1(0,0,0);
		dfs2(0, 0, 0);
		printf("Case #%d: ", cas++);
		printf("%d %d\n", ans1,ans2);
	}
	return 0;
}