#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int TC, n, p[1001];
int g(int x){
	int ans = 0;
	for(int i = 0; i < n; ++i){
		if(x < p[i]){
			ans += (p[i]/x) + (int)(p[i]%x > 0) - 1;
			//printf("%d: %d, %d\n", i, p[i], ans);
		}
	}
	//printf("%d: %d\n", x, ans);
	return ans + x;
}
int main(){
	scanf("%d", &TC);
	for(int tc = 1; tc <= TC; ++tc){
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) scanf("%d", &p[i]);/*
		int top = *max_element(p, p+n), bot = 1;
		//printf("top, bot = %d, %d\n", top, bot);
		while(top > bot+1){
			int l = (top+ 2*bot)/3, r =  top - (top-bot)/3;
			//printf("(%d %d) - (%d %d)\n", bot, top, l, r);
			int x = g(l), y = g(r);
			//printf("%d: %d, %d: %d\n", l, x, r, y);
			if(x < y) top = r-1;
			else if(x > y) bot = l+1;
			else bot++, top--;
		}
		int x = g(top), y = g(bot), z = g((top+bot)/2);
		if(x <= min(y, z)) printf("Case #%d: %d\n", tc, x);
		else if(y <= min(x, z)) printf("Case #%d: %d\n", tc, y);
		else if(z <= min(y, x)) printf("Case #%d: %d\n", tc, z);
		else{
			printf("CATASTROPHIC FAILURE\n");
			return 0;
		}*/
		int ans = 1000000000;
		for(int i = 1; i <= 1000; ++i) ans = min(ans, g(i));
		printf("Case #%d: %d\n", tc, ans);
	}
}