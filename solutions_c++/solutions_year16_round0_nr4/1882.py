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
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << t1 << ": ";
		for (int i = 1; i <= k; i++)
			cout << i << " ";
		cout << endl;
	}
	return 0;
}