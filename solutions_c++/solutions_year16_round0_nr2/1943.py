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
		string str;
		cin >> str;
		int cnt = 0;
		while (1) {
			bool flag = true;
			int last = -1;
			for (int i = str.length()-1; i >= 0; i--) {
				if (str[i] == '-') {
					flag = false;
					last = i;
					break;
				}
			}
			if (flag)
				break;
			if (str[0] == '+') {
				cnt++;
				for (int i = 0; i < str.length(); i++) {
					if (str[i] != '+') {
						break;
					}
					else {
						str[i] = '-';
					}
				}
			}
			for (int i = 0; i <= last; i++) {
				if (str[i] == '-')
					str[i] = '+';
				else
					str[i] = '-';
			}
			string tmp = str;
			for (int i = 0; i <= last; i++)
				tmp[i] = str[last-i];
			str = tmp;
			cnt++;
		}
		printf("Case #%d: %d\n", t1, cnt);
	}
	return 0;
}