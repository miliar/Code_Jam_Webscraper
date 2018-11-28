#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <list>
using namespace std;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testsCnt, a[4][4], r1, r2;
	set<int> sa, sb, ss;
	scanf("%d", &testsCnt);
	for (int testN = 1; testN <= testsCnt; testN++) {
		sa.clear();
		sb.clear();
		ss.clear();
		scanf("%d", &r1);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &a[i][j]);
				if (i + 1 == r1)
					sa.insert(a[i][j]);
			}
		}
		scanf("%d", &r2);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &a[i][j]);
				if (i + 1 == r2)
					sb.insert(a[i][j]);
			}
		}
		for (int i = 1; i <= 16; i++)
			if (sa.find(i) != sa.end() && sb.find(i) != sb.end())
				ss.insert(i);
		printf("Case #%d: ", testN);
		if (ss.size() == 0)
			printf("Volunteer cheated!\n");
		else if (ss.size() > 1)
			printf("Bad magician!\n");
		else
			printf("%d\n", *ss.begin());
	}	

}
