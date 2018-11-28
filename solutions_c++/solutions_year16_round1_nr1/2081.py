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
		string res = "";
		res = res + str[0];
		for (int i = 1; i < str.length(); i++) {
			if ((int)str[i] >= (int)res[0]) {
				string temp = "";
				temp = temp + str[i];
				temp = temp + res;
				res = temp;
			}
			else {
				res = res + str[i];
			}
		}
		cout << "Case #" << t1 << ": " << res << endl;
	}
	return 0;
}