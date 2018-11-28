#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <time.h>
#include <string>
#include<bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <deque>
#include <map>
using namespace std;
typedef long long ll;
const int N = 1000 + 10;
char str[N];
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t, cas = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%s", str);
		deque<char> q;
		for (int i = 0; str[i]; ++i)
			if (q.empty() || q.front() > str[i])
				q.push_back(str[i]);
			else
				q.push_front(str[i]);
		string ans = "";
		while (q.size()) {
			ans += q.front();
			q.pop_front();
		}
		printf("Case #%d: %s\n", cas++, ans.c_str());
	}

	return 0;
}