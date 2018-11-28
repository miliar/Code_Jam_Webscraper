#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int map[2][4][4];
vector <int> ans;
int cas = 0;
int T;
int n;
int m;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);
	while(T--) {
		scanf("%d", &n);
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) scanf("%d", &map[0][i][j]);
		}
		scanf("%d", &m);
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) scanf("%d", &map[1][i][j]);
		}
		ans.clear();
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) if(map[0][n-1][i] == map[1][m-1][j]) ans.push_back(map[0][n-1][i]);
		}
		printf("Case #%d: ", ++cas);
		if(ans.size() == 0) puts("Volunteer cheated!");
		if(ans.size() == 1) printf("%d\n", ans[0]);
		if(ans.size() > 1) puts("Bad magician!");
	}
	return 0;
}
