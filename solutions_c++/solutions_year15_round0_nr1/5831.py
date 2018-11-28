#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int iii, j, nnn, t;
	int res;
	string str;
	scanf("%d", &t);
	for (int l = 1; l <= t; l++) {
		res = 0;
		str = "";
		cin >> nnn >> str;
		j = (str[0] - '0');
		for (iii = 1; iii <= nnn; iii++) {
			if (j < iii && str[iii] != '0') {
				res += (iii - j);
				j = iii;
			}
			j += (str[iii] - '0');
		}
		printf("Case #%d: %d\n", l, res);
	}
	return 0;
}