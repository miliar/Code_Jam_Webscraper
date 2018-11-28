#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++) {
		int r;
		scanf("%d", &r);
		r--;
		bool a[17];
		fill(a+1, a+17, false);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				int x; scanf("%d", &x);
				if(i==r) a[x] = true;
			}
		}
		scanf("%d", &r);
		r--;
		int cnt = 0, ans = 0;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				int x; scanf("%d", &x);
				if(i==r && a[x]) { cnt++; ans = x; }
			}
		}
		printf("Case #%d: ", t);
		if(cnt==1) printf("%d\n", ans);
		else if(cnt==0) puts("Volunteer cheated!");
		else puts("Bad magician!");
	}
	return 0;
}
