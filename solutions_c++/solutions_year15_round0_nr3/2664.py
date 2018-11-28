#include <cstdio>
const int maxn = 10000 + 10;
char ss[maxn];
int ans[maxn];
int s[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int L, X;

bool find(int ijk, int cur) { // if find ijk ,return position
	if(ijk == 5) {
		if(ans[L*X - 1] == -1) return true;
		else return false;
	}else {
		for(int i = cur; i < L*X; i++) {
			if(ans[i] == ijk) {
				if(ijk == 2) {if(find(4, cur+1)) return true;}
				else if(ijk == 4) {if(find(5, cur+1)) return true;}
			}
		}
	}
	return false; // not found ijk
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T, cnt = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d %d %s", &L, &X, ss);
		int sign = 0, t;
		ans[0] = ss[0] - 'g';
		for(int i = 1; i < L*X; i++) {
			if(ans[i-1] > 0) {sign = 1; t = ans[i-1];}
			else {sign = -1; t = -ans[i-1];}
			ans[i] = s[t][ss[i%L] - 'g'] * sign;
		}
		if(find(2, 0)) {
			printf("Case #%d: YES\n", cnt++);
		}else {
			printf("Case #%d: NO\n", cnt++);
		}
	}
	return 0;
}