#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

const int Maxl = 200005;

int t;
string str;
char S[Maxl];
int slen;

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		cin >> str;
		int res = 0;
		slen = 0;
		for (int i = 0; i < str.length(); i++)
			if (slen == 0 || S[slen - 1] != str[i])
				S[slen++] = str[i];
			else { slen--; res += 10; }
		res += slen / 2 * 5;
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}