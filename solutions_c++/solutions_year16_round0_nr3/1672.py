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

long long check_prime(long long val) {
	if (val < 2)
		return 0LL;
	for (long long i = 2; i <= sqrt(val); i++) {
		if (val % i == 0)
			return i;
	}
	return 0LL;
}

int main()
{
	long long power[36];
	power[0] = 1LL;
	for (int i = 1; i < 34; i++)
		power[i] = power[i-1]*2LL;

	int t;
	cin >> t;
	for (int t1 = 1; t1 <= t; t1++) {
		int n, k;
		cin >> n >> k;
		cout << "Case #" << t1 << ":\n";
		for (int i = power[n-1]; (i < power[n]) && (k > 0); i++) {
			if (i&1) {
				vector < long long > v1;
				for (int base = 2; base <= 10; base++) {
					long long answer = 0;
					long long val = 1;
					for (int j = 0; j < n; j++) {
						if (i & (1 << j)) {
							answer = answer + val;
						}
						val = val*base;
					}
					long long check_pm = check_prime(answer);
					if (check_pm > 1LL)
						v1.push_back(check_pm);
					else 
						break;
				}
				if ((int)v1.size() == 9) {
					for (int j = n-1; j >= 0; j--) {
						if (i & (1 << j))
							cout << 1 ;
						else
							cout << 0 ;
					}
					cout << " ";
					for (int j = 0; j < 9; j++) 
						cout << v1[j] << " ";
					cout << endl;
					k--;
				}
			}
		}
	}
	return 0;
}