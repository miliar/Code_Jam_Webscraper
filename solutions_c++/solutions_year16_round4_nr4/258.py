#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 30;

int n;
char s[MAXN][MAXN], s0[MAXN][MAXN];

int ans;

int a[MAXN], vis[MAXN];

bool DFS2(int d){
	if (d == n)
		return true;
	int cnt = 0;
	for (int i = 0; i < n; ++i)
		if (!vis[i] && s[a[d]][i] == '1'){
			++cnt;
			vis[i] = true;
			if (!DFS2(d + 1))
				return false;
			vis[i] = false;
		}
	return cnt;
}

bool check(){
	for (int i = 0; i < n; ++i)
		a[i] = i;
	bool ret = true;
	do{
		for (int i = 0; i < n; ++i)
			vis[i] = false;
		ret &= DFS2(0);
	}
	while (ret && next_permutation(a, a + n));
	return ret;
}

void DFS(int d, int sum){
	if (d == n * n){
		if (check() && ans > sum)
			ans = sum;
		return;
	}
	
	int x = d / n, y = d % n;
	if (s[x][y] == '1')
		DFS(d + 1, sum);
	else{
		DFS(d + 1, sum);
		s[x][y] = '1';
		DFS(d + 1, sum + 1);
		s[x][y] = '0';
	}
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%s", s[i]);
		ans = 16;
		DFS(0, 0);
		printf("%d\n", ans);
	}
	return 0;
}

