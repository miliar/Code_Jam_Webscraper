#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long lint;
lint fair[10000010];
int t = 0;

bool isPalindrome(lint k) {
	char str[20];
	sprintf(str, "%lld", k);
	int s = strlen(str);
	for (int i = 0, j = s-1; i <= j; ++i, --j) {
		if (str[i] != str[j]) return false;
	}
	return true;
}

void preprocess() {
	for (lint i=1; i < 10000002; ++i) {
		if (!isPalindrome(i))
			continue;
		lint j = i*i;
		if (!isPalindrome(j))
			continue;
		fair[t++] = j;
	}
}

int main() {
	preprocess();
	int cases, cn = 0;
	scanf("%d",&cases);
	while (cases--) {
		lint a, b;
		scanf("%lld%lld",&a,&b);
		int i = lower_bound(fair, fair+t, a) - fair;
		int j = upper_bound(fair, fair+t, b) - fair;
		printf("Case #%d: %d\n", ++cn, j-i);
	}

	return 0;
}