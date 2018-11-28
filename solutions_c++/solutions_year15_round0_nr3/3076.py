#include <cstdio>
#include <string>
using namespace std;

char org[10010];
int len;

int a[4][4] = {1, 2, 3, 4, 2, -1, 4, -3, 3, -4, -1, 2, 4, 3, -2, -1};

bool dfs(int cur, int whi){
	int tmp = org[cur];
	if (whi < 4 && tmp == whi) {
		bool ans = dfs(cur + 1, whi + 1);
		if (ans) return 1;
	}
	for (int i = cur + 1; i < len; i++){
		if (tmp > 0) tmp = a[tmp - 1][org[i] - 1];
		else tmp = -a[-tmp - 1][org[i] - 1];
		if (whi < 4 && tmp == whi) {
			bool ans = dfs(i + 1, whi + 1);
			if (ans) return 1;
		}
	}
	if (whi == 4 && tmp == whi) return 1;
	return 0;
}

int main(){
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int l, x;
		char str[10010];
		scanf("%d %d", &l, &x);
		scanf("%s", str);
		len = strlen(str);
		for (int i = 0; i < x; i++) {
			strcpy(org + i * len, str);
		}
		len = strlen(org);
		for (int i = 0; i < len; i++) {
			if (org[i] == 'i') org[i] = 2;
			else if (org[i] == 'j') org[i] = 3;
			else if (org[i] == 'k') org[i] = 4;
			else org[i] = 1;
		}
		bool result = dfs(0, 2);
		if (result) {
			printf("Case #%d: YES\n", t + 1);
		}
		else {
			printf("Case #%d: NO\n", t + 1);
		}
	}
}