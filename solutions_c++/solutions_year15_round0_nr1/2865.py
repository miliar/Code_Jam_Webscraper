#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <iostream>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

char s[10005];

int main() {
int c;
	scanf("%d",&c);
	for (int z = 1; z <= c; ++z) {
		int n;
		scanf("%d%s",&n,s);
		int now = 0, answer = 0;
		for (int i = 0; i <= n; ++i) {
			if (s[i] > '0') {
				if (now < i) {
					answer += i - now;
					now = i;
				}
				now += s[i] - '0';
			}
		}
		printf("Case #%d: %d\n",z, answer);
	}
	return 0;
}
		
