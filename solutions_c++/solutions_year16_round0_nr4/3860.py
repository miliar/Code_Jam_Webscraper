#include <cstdio>

using namespace std;

int main(void){
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int cas, cc=0, k, c, s;
	
	scanf("%d", &cas);
	while( cas-- ){
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", ++cc);
		for(int i=1; i<=k; ++i)
			printf(" %d", i);
		putchar('\n');
	}
	
	return 0;
}

