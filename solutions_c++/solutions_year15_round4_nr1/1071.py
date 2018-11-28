#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

using namespace std;

typedef long long LL;

const int maxn = 233;
const int dr[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

char mp[maxn][maxn];

int main(){
	int T;
	scanf("%d", &T);
	for (int TI = 1; TI <= T; ++TI){
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i)
			scanf("%s", mp[i] + 1);
		int ans = 0;
		bool flag = 0;
		for (int i = 1; i <= n && !flag; ++i)
			for (int j = 1; j <= m && !flag; ++j)
				if (mp[i][j] != '.'){
					int pos;
					if (mp[i][j] == '>') pos = 0;
					if (mp[i][j] == 'v') pos = 1;
					if (mp[i][j] == '<') pos = 2;
					if (mp[i][j] == '^') pos = 3;
					flag = 1;
					for (int k = 0; k < 4; ++k)
						for (int x = i + dr[k][0], y = j + dr[k][1]; x > 0 && x <= n && y > 0 && y <= m; x += dr[k][0], y += dr[k][1])
							if (mp[x][y] != '.'){
								flag = 0;
								if (k == pos) --ans;
								break;
							}
					++ans;
				}
		printf("Case #%d: ", TI);
		if (flag) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
