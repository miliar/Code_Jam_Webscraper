#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <set>


#define rep(i, n) for(int i = 0; i < n; i ++)
typedef long long LL;

int main() {
  // freopen("input.txt", "r", stdin);
 //   freopen("out.txt", "w", stdout);
    int T, n;
    scanf("%d", &T);
    rep(cas, T) {
    	scanf("%d", &n);
    	int now = 0, add = 0;
    	for(int i = 0; i <= n; i ++) {
    		int x;
    		scanf("%1d", &x);
			if(now < i && x) {
				add += i - now;
				now = i;
			}
			now += x;
    	}
    	printf("Case #%d: %d\n", cas + 1, add);
    }
    return 0;
}
