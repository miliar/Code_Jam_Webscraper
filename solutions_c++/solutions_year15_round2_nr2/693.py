#include <cstdio>
#include <cstring>

int R, C, n;
bool map[20][20];

int ans;

void DFS(int d, int cnt){
	if (d == R * C){
		if (cnt < n)
			return;
		int sum = 0;
		for (int i=0;i<R;++i)
			for (int j=0;j<C;++j)
				if (map[i][j]){
					sum += map[i + 1][j];
					sum += map[i][j + 1];
				}
		if (ans > sum)
			ans = sum;
		return;
	}

	map[d / C][d % C] = false;
	DFS(d + 1, cnt);
	if (cnt < n){
		map[d / C][d % C] = true;
		DFS(d + 1, cnt + 1);
		map[d / C][d % C] = false;
	}
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi=1;casi<=cas;++casi){
		scanf("%d%d%d", &R, &C, &n);
		ans = R * C * 100;
		memset(map, 0, sizeof(map));
		DFS(0, 0);
		printf("Case #%d: %d\n", casi, ans);
	}
	return 0;
}
