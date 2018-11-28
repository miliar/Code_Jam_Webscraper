#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

char s[1005];
vector<char> a, b;
int main() {
	int t, cas = 0;
	int i, j, k;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%s", &s);
		char last = s[0];
		a.clear();
		b.clear();
		a.push_back(s[0]);
		for (int i = 1; s[i]; ++i) {
			if (s[i] >= last) {
				a.push_back(s[i]);
				last = s[i];
			} else {
				b.push_back(s[i]);
			}
		}
		printf("Case #%d: ", cas);
		for (i = a.size() - 1; i >= 0; --i)
			printf("%c", a[i]);
		for (i = 0; i < b.size(); ++i)
			printf("%c", b[i]);
		puts("");
	}
}
