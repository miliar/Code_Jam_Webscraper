#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <cstring>
#include <string>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

int n, t;
int grid[17];
int main () {
	scanf("%d", &t);
	for (int _ = 1; _ <= t; _++){
		printf("Case #%d: ", _);
		memset(grid, 0, sizeof grid);
		int a, b, c;
		for(c = 0; c < 2; ++c){
		scanf("%d", &a);
		for (int i = 1; i < 5; ++i) {
			for(int j = 1; j < 5; ++j) {
				scanf("%d", &b);
				if (i == a) grid[b]++;
			}
		}
		}
		c = 0;
		for(int i = 1; i < 17; ++i){
			if(grid[i] > 1) {
				c++;
				n = i;
			}
		}
		if(c == 0) printf("Volunteer cheated!\n");
		else if(c > 1) printf("Bad magician!\n");
		else printf("%d\n", n);
	}
return 0;
}