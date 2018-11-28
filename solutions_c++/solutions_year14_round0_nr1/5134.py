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
//#include <cstdio>
//#include <cstring>
//#include <algorithm>
//using namespace std;
//#define maxn 50005
//int n, m;
//int s;
//int a[maxn],sum[maxn];
//int find(int x){ if (x != sum[x]) return sum[x] = find(sum[x]); }
//void search(int x, int y){
//	int fx = find(x), fy = find(y);
//	if (fx != fy)sum[fy] = fx;
//}
//int main(){
//	int t;
//	scanf("%d", &t);
//	while (t--){
//		scanf("%d%d", &n, &m);
//		s = 0;
//		for (int i = 0; i <= n; i++)sum[i] = i;
//		memset(a, -1, sizeof a);
//		for (int i = 0; i < m; i++){
//			int op, x, y;
//			scanf("%d%d%d", &op, &x, &y);
//			int fx = find(x), fy = find(y);
//			if (op == 1){
//				if (x>n || y > n || a[fx] != -1 && a[fy] != -1 && a[fx] != a[fy]){ s++; continue; }
//				if (x == y || fx == fy)continue;
//				search(x, y);
//				fx = find(x);
//				if (a[fx] == -1)a[fx] = a[fy];
//			}
//			else{
//				if (x > n || y > n || x == y || fx == fy || a[fx] != -1 && a[fy] != -1 && (a[fx] >= a[fy] && a[fx] != 2 || a[fx] == 2 && a[fy] != 0)){ s++; continue; }
//				if (a[fx] == -1 && a[fy] == -1)a[fx] = 0, a[fy] = 1;
//				else if (a[fx] == -1 && a[fy] != -1)a[fx] = (a[fy] - 1 + 3) % 3;
//				else if (a[fx] != -1 && a[fy] == -1)a[fy] = (a[fx] + 1) % 3;
//			}
//		}
//		printf("%d\n", s);
//	}
//	return 0;
//}


#include <cstdio>
#include <cstring>
int a[5][5],b[5][5];
int n, m, t, s, k;
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas = 1;
	scanf("%d", &t);
	while (t--){
		scanf("%d", &n);
		n--;
		s = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				scanf("%d", &a[i][j]);
			}
		scanf("%d", &m);
		m--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				scanf("%d", &b[i][j]);
			}
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				if (a[n][i] == b[m][j])s++,k=i;
			}
		printf("Case #%d: ", cas++);
		if (s == 1)printf("%d\n", a[n][k]);
		else if (s == 0)printf("Volunteer cheated!\n");
		else if (s>1)printf("Bad magician!\n");
	}
	return 0;
}