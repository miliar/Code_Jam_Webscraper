#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int cnt;
bool flag[10];

void solve(int x) {
	while(x) {
		int y = x % 10;
		if(flag[y] == false) {
			flag[y] = true;
			cnt++;
		}
		x = x / 10;
	}
}

int main() {
	int n;
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&n);
	for(int i = 1;i <= n;i++) {
		int x;
		scanf("%d",&x);
		printf("Case #%d: ",i);
		if(x == 0) 
			printf("INSOMNIA\n");
		else {
			int now = x;
			cnt = 0;
			memset(flag,false,sizeof(flag));
			solve(now);
			while(cnt < 10) {
				now += x;
				solve(now);
			}
			printf("%d\n",now);
		}
	}
	return 0;
}