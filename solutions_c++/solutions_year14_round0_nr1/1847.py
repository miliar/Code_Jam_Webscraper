/*
 * Author    : ben
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <functional>
#include <numeric>
#include <cctype>
using namespace std;
int num[17];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, tmp;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		memset(num, 0, sizeof(num));
		int a, b;
		scanf("%d", &a);
		for(int i = 1; i <= 4; i++) {
			for(int j = 0; j < 4; j++) {
				scanf("%d", &tmp);
				if(i == a) {
					num[tmp]++;
				}
			}
		}
		scanf("%d", &b);
		for(int i = 1; i <= 4; i++) {
			for(int j = 0; j < 4; j++) {
				scanf("%d", &tmp);
				if(i == b) {
					num[tmp]++;
				}
			}
		}
		printf("Case #%d: ", t);
		int ans = count(num, num + 17, 2);
		if(ans == 1) {
			ans = find(num, num + 17, 2) - num;
			printf("%d\n", ans);	
		} else if(ans == 0) {
			printf("Volunteer cheated!\n");
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}


