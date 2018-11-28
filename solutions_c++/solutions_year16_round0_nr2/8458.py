#include <cstdio>
#include <cstring>
#define f(a, b, c) for(int a = b; a < c; a++)

int t, n;
char s[105], e;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	f(i, 1, t + 1){
		scanf("%s", &s);
		e = strlen(s);
		int gg = 0, ans = 0;
		if(s[0] == '-') ans--;
		f(i, 0, e){
			if(s[i] == '-' && gg == 0){
				gg = 1;
				ans += 2;
			}
			if(s[i] == '+')
				 gg = 0;
			//printf("(%d, %d)   ", i, ans);
		}
		printf("Case #%d: %d\n", i, ans);
	}
	scanf("\n");
}
