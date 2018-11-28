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

int main()
{
	int t;
	cin >> t;
	for (int t1 = 1; t1 <= t; t1++) {
		int n;
		cin >> n;
		int cnt[3000];
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < 2*n-1; i++) {
			for (int j = 0; j < n; j++) {
				int x;
				cin >> x;
				cnt[x]++;
			}
		}
		vector < int > v1;
		for (int i = 0; i < 3000; i++) {
			if (cnt[i] & 1)
				v1.push_back(i);
		}
		cout << "Case #" << t1 << ": ";
		for (int i = 0; i < n-1; i++)
			cout << v1[i] << " ";
		cout << v1[n-1] << endl;
	}
	return 0;
}