#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, k, ans, sum, p;
	char s[1010];
	scanf("%d", &t);
	for (int kase = 1; kase <= t; ++kase) {
	    scanf("%d %s", &k, s);
	    sum = s[0] - '0';
	    ans = 0;
	    for (int i = 1; i <= k; ++i) {
	        if (sum < i && s[i] != '0') {
	        	p = i - sum;
	        	ans += p;
	        	sum += p;
	        }
	        sum += s[i] - '0';
	    }
	    printf("Case #%d: %d\n", kase, ans);
	}

    return 0;
}

/*

*/