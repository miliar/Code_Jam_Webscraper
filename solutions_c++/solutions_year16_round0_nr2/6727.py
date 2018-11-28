#include <iostream>
#include <utility>
#include <limits.h>
#include <fstream>
#include <string>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#define INF 987654321
using namespace std;
typedef long long lld;
char buf[111];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	int result;
	string str;
	scanf("%d",&t);
	for (int TestCase = 1; TestCase <= t; TestCase++) {
		result = 0;
		scanf("%s", buf);
		str = buf;
		int len = str.length();
		for (int length = 1; length < len; length++) {
			if (str[length] != str[length-1]) {
				result++;
			}
			
			
			
		}
		if (str[len - 1] == '-')result++;
		printf("Case #%d: %d\n", TestCase,result);
	}
	return 0;
}

