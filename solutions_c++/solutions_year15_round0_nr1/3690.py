#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int tests,s;
	string str;
	cin >> tests;
	for (int t = 1; t <= tests; t++) {
		cin >> s;
		cin >> str;
		int tot = 0, res = 0;
		for (int i = 0; i < s + 1; i++) {
			int v = (int)(str[i] - '0');
			if (v > 0 && tot < i) {
				res += (i - tot);
				tot = i;
			}
			tot += v;
		}
		printf("Case #%d: %d\n", t, res);
	}
}