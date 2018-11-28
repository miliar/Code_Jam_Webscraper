#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <unordered_map>


using namespace std;


int main() {
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int iii = 0; iii < t; iii++) {
		int n;
		cin >> n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", iii + 1); 
		} else {
			vector<int> c;
			c.resize(10);
			long long sum = n;
			int cnt = 0;
			while (true) {
				long long sum1 = sum;
				while (sum1 > 0LL) {
					if (c[sum1 % 10LL] == 0) {
						c[sum1 % 10LL] = 1;
						cnt++;
					}
					sum1 /= 10LL;
				}
				if (cnt == 10LL) {
					break;
				}
				sum += n;
			}		
			printf("Case #%d: %lld\n", iii + 1, sum); 
		}
	}
    return 0;
}
