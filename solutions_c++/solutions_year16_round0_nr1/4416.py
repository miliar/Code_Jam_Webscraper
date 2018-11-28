#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for (int ii = 1; ii <= t; ii++) {
		printf("Case #%d: ",ii);
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		long long cnt = 100000;
		set<int> s;
		long long temp = n;
		int flag = 0;
		while(cnt--) {
			long long x = temp;
			while(x) {
				s.insert(x%10);
				x /= 10;
			}
			if (s.size() == 10) {
				flag = 1;
				printf("%lld\n",temp);
				break;
			}
			temp += n;
		}
		if (flag == 0) {
			printf("INSOMNIA\n");
		}
	}
}