#include <cstdio>
#include <cstring>


char buf[255];

int main(){
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int t; scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++){
		int n, l; 
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &l);
		bool imp = false;
		for (int i = 0; i < n ;i++) {
			scanf("%s", buf);
			bool ok = false;
			for (int j = 0; j < l; j++) {
				if (buf[j] == '0') {
					ok = true; 
				} 
			}
			if (!ok) 
				imp = true;
		}
		scanf("%s", buf);
		if (imp) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		for (int i = 0; i < l / 2; i++)
			printf("10");
		printf("?");
		printf("1 ");
		if (l != 1)
		for (int i = 0; i < l - 1; i++)
			printf("?");
		else
			printf("0");
		puts("");
		
	}
}