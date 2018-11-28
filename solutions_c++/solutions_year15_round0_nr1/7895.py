#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <set>
#include <stack>
#include <memory.h>
#include<queue>
#include <math.h>
#include <map>
#include <iomanip>
using namespace std;
typedef vector<int> vec;
typedef long long LL;
typedef vector<vector<int> > graph;
#define filla(x,y) memset(x,y,sizeof(x));
#define all(A) A.begin(),A.end()
const double PI = acos(-1.0);
LL gcd(LL a, LL b) {
	if (!b)
		return a;
	return gcd(b, a % b);
}
LL lcm(LL a, LL b) {
	return a * b / gcd(a, b);
}
int sum[1001];
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt2.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int x = 1; x <= t; ++x) {
		filla(sum, 0);
		int a, res = 0;
		string s;
		cin >> a >> s;
		sum[0] += s[0] - '0';
		for (int i = 1; i <= a; ++i) {
			if (s[i] - '0')
				if (sum[i - 1] < i)
					res += (i - sum[i - 1]), sum[i - 1] += (i - sum[i - 1]);
			sum[i] += sum[i - 1] + (s[i] - '0');
		}
		printf("Case #%d: %d\n", x, res);
	}
	return 0;
}
