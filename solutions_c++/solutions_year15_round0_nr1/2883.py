#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
char str[1005];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int tc, Tc = 0;
	scanf("%d", &tc);
	while(tc --){
		scanf("%d%s", &n, str);
		int cur = str[0] - 48, ret = 0;
		for(int i = 1;i <= n;i ++){
			int v = str[i] - 48;
			if(cur < i) ret += i - cur, cur = i;
			cur += v;
		}
		printf("Case #%d: %d\n", ++ Tc, ret);
	}
	return 0;
}

		
