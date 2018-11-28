#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <memory.h>
#include <stdlib.h>
#include <time.h>

typedef long long ll;

const int N = 1e5+3;
const int inf = 1e9;

using namespace std;

char s[N];
int solve()
{
	int n, ans =0, c=0;
	scanf("%d%s",&n,&s);
	for(int i=0;i<n+1;++i) {
		if (c<i && s[i] != '0') {
			ans += i - c;
			c = i;
		}
		c += s[i] - '0';
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	int t;
	scanf("%d",&t);
	for(int i = 0; i < t; ++i)
		printf("Case #%d: %d\n", i+1, solve());
	return 0;
}