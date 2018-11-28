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
	int x, t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt){
		cin >> x;
		if(!x){
			printf("Case #%d: INSOMNIA\n", tt);
			continue;
		}
		bool vis[10] = {};
		int cnt = 0, ans = -1;
		for(int i = 1;; ++i){
			int xx = x * i;
			while(xx){
				if(!vis[xx%10]){
					++cnt;
					vis[xx%10] = 1;
				}
				xx /= 10;
			}
			if(cnt == 10) {
				ans = i;
				break;
			}
		}
		printf("Case #%d: %d\n", tt, ans*x);
	}
}