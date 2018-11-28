#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <utility>
#include <algorithm>

#define			OK			std::cout << "------------" << std::endl;
#define			DEBUG(x)		std::cout << #x << " = " << x << std::endl;

using namespace std;

int m1[4][4], m2[4][4];

int main()
{
	int T;
	scanf("%d", &T);

	for (int _ = 1;_ <= T;_ ++) {
		printf("Case #%d: ", _);
		int N1, N2;
		scanf("%d", &N1);
		N1--;
		for (int i = 0;i < 4;i++) {
			for (int j = 0;j < 4;j++) {
				scanf("%d", &m1[i][j]);
			}
		}

		scanf("%d", &N2);
		N2--;
		for (int i = 0;i < 4;i++) {
			for (int j = 0;j < 4;j++) {
				scanf("%d", &m2[i][j]);
			}
		}
		int cnt = 0, who = 0;
		for (int i = 0;i < 4;i++) {
			for (int j = 0;j < 4;j++) {
				if (m1[N1][i] == m2[N2][j]) {
					cnt ++;
					who = m1[N1][i];
				}
			}
		}
		if (cnt == 0) {
			puts("Volunteer cheated!");
		} else if (cnt == 1) {
			printf("%d\n", who);
		} else {
			puts("Bad magician!");
		}
	}

	return 0;
}
