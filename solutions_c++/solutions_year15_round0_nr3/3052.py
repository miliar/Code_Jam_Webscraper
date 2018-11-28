#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

const int MAXL = 10100;

const short int res[4][4] = {
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0}
};

const bool mns[4][4] = {
	{0, 0, 0, 0},
	{0, 1, 0, 1},
	{0, 1, 1, 0},
	{0, 0, 1, 1}
};

int l, x;
char s[MAXL];
short int d[MAXL];

short int dp[MAXL][4][4][2];

void read() {
	scanf("%d %d\n", &l, &x);
	scanf("%s", &s);
}

short int decode(char ch) {
	switch(ch) {
		case 'i': return 1;
		case 'j': return 2;
		case 'k': return 3;
		default: return -1;
	}
}

short int go(int pos, int ready, int p, bool signs) {
	short int &ret = dp[pos][ready][p][signs];
	
	if(ret != -1)
		return ret;
	
	if(pos == l * x) {
		if(ready == 2 && p == 3 && !signs) ret = 1;
		else ret = 0;
		
		return ret;
	}
	
	if(go(pos + 1, ready, res[p][ d[pos] ], signs ^ mns[p][ d[pos] ])) {
		ret = 1;
		return ret;
	}
	
	if(ready == 0 && p == 1 && !signs && go(pos + 1, ready + 1, d[pos], 0)) {
		ret = 1;
		return ret;
	}
	
	if(ready == 1 && p == 2 && !signs && go(pos + 1, ready + 1, d[pos], 0)) {
		ret = 1;
		return ret;
	}
	
	ret = 0;
	return ret;
}

void solve() {
	for(int i = l; i < l * x; i ++)
		s[i] = s[i - l];
	
	for(int i = 0; i < l * x; i ++)
		d[i] = decode(s[i]);
	
	memset(dp, -1, sizeof(dp));
	
	if(go(0, 0, 0, 0)) printf("YES\n");
	else printf("NO\n");
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int iter = 1; iter <= t; iter ++) {
		printf("Case #%d: ", iter);
		read();
		solve();
	}

    return 0;
}
