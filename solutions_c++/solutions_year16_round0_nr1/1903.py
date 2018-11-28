/*
Author : lifecodemohit
*/

#ifdef __APPLE__

    #include <cassert>
    #include <iostream>
    #include <iomanip>
    #include <ctime>
    #include <cstdio>
    #include <vector>
    #include <algorithm>
    #include <utility>
    #include <queue>
    #include <stack>
    #include <string>
    #include <cstring>
    #include <sstream>
    #include <map>
    #include <set>
    #include <unordered_map>
    #include <unordered_set>

#else

    #include <bits/stdc++.h>

#endif  

using namespace std;

void add_digit(int cnt[], long long answer) {
	if (answer == 0) {
		cnt[0]++;
		return ;
	}
	while (answer > 0) {
		cnt[answer%10]++;
		answer = answer/10;
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int t1 = 1; t1 <= t; t1++) {
		long long n;
		scanf("%lld", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", t1);
		}
		else {
			bool flag = false;
			long long MAXX = 2000000;
			int cnt[11];
			memset(cnt, 0, sizeof(cnt));
			for (long long it = 1LL; it <= MAXX; it++) {
				long long answer = it*n;
				add_digit(cnt, answer);
				bool mark = true;
				for (int j = 0; j < 10; j++) {
					if (cnt[j] == 0) {
						mark = false;
						break;
					}
				}
				if (mark) {
					flag = true;
					printf("Case #%d: %lld\n", t1, answer);
					break;
				}
			}
			if (!flag)
				printf("Case #%d: INSOMNIA\n", t1);
		}
	}
	return 0;
}