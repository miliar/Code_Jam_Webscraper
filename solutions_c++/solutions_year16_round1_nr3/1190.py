#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int bff[1000], vis[1000];

int start, n, ans;

void brute(int pos, int l, int len) {
	vis[pos] = 1;
	int mybff = bff[pos];
	if (mybff == start || mybff == l)
		if (ans < len)
			ans = len;
	
	if (mybff != l) {
		if (!vis[mybff])
			brute(mybff, pos, len+1);
	}
	else {
		for (int i=0;i<n;i++) {
			if (!vis[i])
				brute(i, pos, len+1);
		}
	}
	vis[pos] = 0;
}

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		printf("Case #%d: ", t);
		cin>>n;
		for (int i=0;i<n;i++) {
			cin>>bff[i];
			bff[i]--;
		}
		ans = 0;
		for(start=0;start<n;start++) {
			brute(start, -1, 1);
		}
		cout << ans << endl;
	}
	return 0;
}
