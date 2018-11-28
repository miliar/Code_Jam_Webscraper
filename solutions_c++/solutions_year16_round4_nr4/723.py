#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
const int N = 5;
char s[N][N];
int ans, n;
bool flag;
int v[N], c[N];
int a[100][2];

bool dfs(int now, int n) {
	//cout<<"dkfj"<<' '<<now<<' '<<n<<endl;
	if (now > n) {
		return true;
	}
	for (int i = 1; i <= n; i++)
		if (c[i] == 0) {
			int k = 0;
			for (int j = 1; j <= n; j++)
				if (s[i][j] == '1' && v[j] == 0) {
					//cout<<i<<' '<<j<<endl;
					c[i] = 1;
					v[j] = 1;
					if (!dfs(now + 1, n)) return false;
					c[i] = 0;
					v[j] = 0;
					k++;
				}
			if (k == 0) return false;
		}
	return true;
}



bool check() {
	memset(c, 0, sizeof(c));
	memset(v, 0, sizeof(v));
	flag = true;
	return dfs(1, n);
}

void dfs(int now, int m, int t) {
	if (now > m) {
		//cout<<t<<endl;
		//for (int i = 1; i <= n; i++)
		//	printf("%s\n", s[i] + 1);
		bool ff = check();
		//cout<<ff<<endl;
		if (ff) {
			ans = min(ans, t);
		}
		return;
	}
	int x = a[now][0], y = a[now][1];
	dfs(now + 1, m, t);
	s[x][y] = '1';
	dfs(now + 1, m, t + 1);
	s[x][y] = '0';
}

int main() {
	int o, cas = 0;
	scanf("%d", &o);
	while (o--) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%s", s[i] + 1);
		int m = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) if (s[i][j] == '0') {
				m++;
				a[m][0] = i;
				a[m][1] = j;
			}
		ans = m;
		dfs(1, m, 0);
		printf("Case #%d: %d\n", ++cas, ans);
	}
}