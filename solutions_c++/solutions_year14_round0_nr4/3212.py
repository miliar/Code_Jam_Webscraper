#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include<cstdlib>
using namespace std;
#define eps 1e-10
#define maxn 100010
#define pi acos(-1.0)
int n;
double a[1005];
double b[1005]; 
int vis[1005];
int main(){
	int t;
	freopen("D-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	int kase = 0;
	while (t--){
		scanf("%d", &n);
		for (int i = 0; i < n; i++){
			scanf("%lf", &a[i]);
		}
		for (int i = 0; i < n; i++){
			scanf("%lf", &b[i]);
		}
		sort(a, a + n);
		sort(b, b + n);
		int ans1 = 0, ans2 = 0;
		for (int i = 1; i <=n; i++){
			bool flag = true;
			for (int j = 0; j < i;j++)
			if (a[n - i + j] < b[j]){
				flag = false; break;
			}
			if (flag)ans1 = i;
			else break;
		}
		memset(vis, 0, sizeof(vis));
		for (int i = 0; i <n; i++){
			for (int j = 0; j < n;j++)
			if (a[i] < b[j]&&vis[j]==0){
				vis[j] = 1;
				ans2++;
				break;
			}
		}
		printf("Case #%d: %d %d\n", ++kase, ans1,n-ans2);
	}
	return 0;
}