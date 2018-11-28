#include <cstdio>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("standout.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		int m;
		scanf("\n%d ", &m);
		int count = 0, out = 0;
		for(int k = 0; k <= m; k++){
			char tmp[2];
			scanf("%c", tmp);
			tmp[1] = '\0';
			out += max(0, k - count);
			count = max(k, count) + atoi(tmp);
		}
		printf("Case #%d: %d\n", i, out);
	}
	return 0;
}

		
