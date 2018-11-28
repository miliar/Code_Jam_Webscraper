#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
using namespace std;

#define S second
#define F first
#define mp make_pair
typedef pair<int, int> PII;
#define pb push_back
typedef long long ll;

int main () {
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt){
		char s[110];
		scanf("%s", s);
		char c = s[0];
		int len = strlen(s), cnt = 0;
		for(int i = 1; i < len; ++i) if(s[i] != c){
			++cnt;
			c = s[i];
		}
		if(c == '-') ++cnt;
		printf("Case #%d: %d\n", tt, cnt);
	}
}