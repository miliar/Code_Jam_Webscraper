#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>

using namespace std;

#define SI ({int __; scanf("%d", &__); __;})

int row[25], sa, sb, cnt;
int main() {
	int TC = SI;
	for(int tc = 1;tc <= TC;++tc) {
		printf("Case #%d: ", tc);
		sa = SI;
		for(int i = 0;i < 16;++i) {
			int a = SI;
			row[a] = i/4;
		}
		sb = SI; --sb; --sa;
		cnt = 0;
		for(int i = 0;i < 4;++i) {
			for(int j = 0;j < 4;++j) {
				int x = SI;
				if(i == sb && row[x] == sa) {
				   ++cnt;
				   row[20] = x;
				}
			}
		}
		if(cnt == 0) puts("Volunteer cheated!");
		else if(cnt == 1) printf("%d\n", row[20]);
		else puts("Bad magician!");
	}
}
