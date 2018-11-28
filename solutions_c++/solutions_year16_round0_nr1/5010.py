#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<set>
#include<unordered_set>
#include<algorithm>
using namespace std;

int n;

void work() {
	if (n == 0) {
		printf("INSOMNIA\n");
		return;
	}

	vector<bool> flag(10, 1);
	int ans = 0, cnt = 0, now;
	
	while (cnt < 10) {
		ans++;
		now = ans * n;
//		printf("%d\n", now);
		while (now > 0) {
			if (flag[now % 10]) {
				flag[now % 10] = false;
				cnt ++;
			}
			now /= 10;
		}
	}
	printf("%d\n", ans * n);
}

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int i=0;i<t;i++) {
		cin >> n;
		printf("Case #%d: ", i+1);
		work();
	}

	return 0;
}

