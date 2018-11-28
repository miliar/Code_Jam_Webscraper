#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <cstring>
#include <math.h>
#include<cstdio>
#include<deque>
#include<sstream>
/*YOU got a DREAM, YOU gotta protect it. */
using namespace std;
int dx[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

int main() {
	freopen("A-large.in" , "rt" , stdin);
	freopen ("out.txt","w",stdout);
	int t, tt = 1;
	cin >> t;
	while (t--) {
		string s;
		int x;
		cin >> x >> s;
		int sum = s[0] - '0', res = 0;
		for (int i = 1; i <= x; i++)
			if (sum >= i) {
				sum += s[i] - '0';
			} else {
				res += (i - sum);
				sum += (i - sum) + s[i] - '0';
			}
		printf("Case #%d: ", tt++);
		cout << res << endl;
	}
	return 0;
}
