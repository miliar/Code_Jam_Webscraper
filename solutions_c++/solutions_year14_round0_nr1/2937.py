#include <cstdio>
#include <cstring>
using namespace std;

int t, n, m, tmp, num, a[20];

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	
	for(int c = 1; c <= t; c++) {
		int ans = 0;
		memset(a, 0, sizeof(int) * 20);
		scanf("%d", &n);
		for(int i = 1; i <= 4; i++) {
			for(int j = 1; j <= 4; j++) {
				scanf("%d", &tmp);
				if(i == n) a[tmp]++;
			}
		}
		scanf("%d", &n);
		for(int i = 1; i <= 4; i++) {
			for(int j = 1; j <= 4; j++) {
				scanf("%d", &tmp);
				if(i == n && a[tmp] == 1) {
					ans++;
					num = tmp;
				} 
			}
		}
		if (ans == 0) printf("Case #%d: Volunteer cheated!\n", c);
		else if (ans == 1) printf("Case #%d: %d\n", c, num);
		else printf("Case #%d: Bad magician!\n", c);
	}
	return 0;
}