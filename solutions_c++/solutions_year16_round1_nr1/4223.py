#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <string.h>
#include <functional>

using namespace std;

int check[11];


int main()
{
	int T;
	char org[4444];
	string ans;
	scanf("%d", &T);
	for (int t = 1;t <= T;t++) {
		scanf("%s", &org);
		int len = strlen(org);
		ans.push_back(org[0]);
		for (int i = 1;i < len;i++) {
			if (org[i] >= ans.front()) {
				ans.insert(ans.begin(), org[i]);
			}
			else {
				ans.push_back(org[i]);
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
		ans.clear();
	}
	return 0;
}