#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <utility>
using namespace std;

int t, T = 1;
char dm;

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d%c", &t, &dm);
	while(t--){
		int smax, ans = 0, cnt = 0;
		char s[1100];
		scanf("%d%c", &smax, &dm);
		gets(s);
		for(int i = 0; i <= smax; i++){
			if(cnt < i){
				ans += i - cnt;
				cnt += i - cnt;
			}
			cnt += s[i] - '0';
		}
		printf("Case #%d: %d\n", T++, ans);
	}
	return 0;
}
