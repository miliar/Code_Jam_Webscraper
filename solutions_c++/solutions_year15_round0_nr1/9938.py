#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int testCases;
	scanf("%d", &testCases);
	for(int t = 1; t < testCases + 1; t++)
	{
		int ans = 0;
		int sMax;
		int currentAudience = 0;
		scanf("%d", &sMax);
		string str;
		cin >> str;
		printf("Case #%d: ", t);
		if (sMax == 0) {
			printf("0\n");
			continue;
		}
		for (int s = 0; s < sMax; s ++) {
			int num0 = str[s] - '0';
			int num1 = str[s+1] - '0';
			if (num1 != 0) {
				if (num0 == 0) {
					if (currentAudience < (s + 1)) {
						ans += (s + 1 - currentAudience);
						currentAudience += (ans);
					}
				} else {
					currentAudience += num0;
				}
			} else {
				currentAudience += num0;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}