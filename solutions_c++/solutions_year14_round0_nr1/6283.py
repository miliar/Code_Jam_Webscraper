#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
using namespace std;
int cnt[17];
inline void work(){
	memset(cnt, 0, sizeof cnt);
	int rw;
	scanf("%d", &rw);
	for (int i = 1; i <= 4; ++ i)
		for (int j = 1; j <= 4; ++ j){
			int t;
			scanf("%d", &t);
			if (i == rw)
				++ cnt[t];
		}
	scanf("%d", &rw);
	for (int i = 1; i <= 4; ++ i)
		for (int j = 1; j <= 4; ++ j){
			int t;
			scanf("%d", &t);
			if (i == rw)
				++ cnt[t];
		}
	int ans = -1;
	for (int i = 1; i <= 16; ++ i)
		if (cnt[i] == 2)
			if (ans == -1)
				ans = i;
			else
				ans = -2;
	if (ans == -1)
		puts("Volunteer cheated!");
	else if (ans == -2)
		puts("Bad magician!");
	else
		printf("%d\n", ans);
	
}
int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++ cases){
		printf("Case #%d: ", cases);
		work();
	}
}
