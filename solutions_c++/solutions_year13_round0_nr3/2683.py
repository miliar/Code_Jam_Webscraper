#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <time.h>
using namespace std;

bool isp(int x) {
	string a, b;
	while (x) {
		a.push_back('0' + (x % 10) );
		x /= 10;
	}
	b = string(a.rbegin(), a.rend() );
	return (a == b);
}

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; ++t) {
		int a, b;
		cin >> a >> b;
		int cnt = 0;
		for (int i = 1; i * i <= b; ++i) {
			if (i * i < a) continue;
			if (isp(i * i) && isp(i) ) {
				++cnt;
			}
		}
		printf("Case #%d: %d\n", t, cnt);
	}
				
	return 0;
}
