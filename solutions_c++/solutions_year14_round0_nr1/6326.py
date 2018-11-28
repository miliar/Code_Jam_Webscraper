#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

int a[5][5], b[5][5], x, y;
int main() {
	int T;
	scanf("%d", &T);
	for(int it = 1;it <= T; ++it) {
		scanf("%d", &x);
		for(int i = 1;i <= 4; ++i)
			for(int j = 1;j <= 4; ++j) 
				scanf("%d", &a[i][j]);
		scanf("%d", &y);
		for(int i = 1;i <= 4; ++i)
			for(int j = 1;j <= 4; ++j) 
				scanf("%d", &b[i][j]);

		set<int> first;
		int ret = -1, cnt = 0;
		for(int i = 1;i <= 4; ++i)
			first.insert(a[x][i]);
		for(int i = 1;i <= 4; ++i) {
			if(first.find(b[y][i]) != first.end()) {
				cnt ++;
				ret = b[y][i];
			}
		}
		printf("Case #%d: ", it);
		if(cnt == 1) printf("%d\n", ret);
		else if(cnt > 1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}

}
