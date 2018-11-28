
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i8;

int tst, R,C, bo[105][105];
int mar[105], mac[105];

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		scanf("%d%d",&R,&C);
		fill(mar,mar+R,0);
		fill(mac,mac+C,0);
		
		for (int r=0; r<R; r++)
			for (int c=0; c<C; c++) {
				scanf("%d", &bo[r][c]);
				mar[r]=max(mar[r],bo[r][c]);
				mac[c]=max(mac[c],bo[r][c]);
			}		
		
		bool ok=true;
		for (int r=0; r<R; r++)
			for (int c=0; c<C; c++)
				if (bo[r][c]<mar[r] && bo[r][c]<mac[c]) ok=false;
				
		printf("Case #%d: %s\n", cas, ok?"YES":"NO");
	}
}
