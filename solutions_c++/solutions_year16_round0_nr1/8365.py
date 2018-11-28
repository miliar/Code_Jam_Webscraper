#include <cstdio>
#define f(a, b, c) for(int a = b; a < c; a++)

int t, n, l[12], c, ans;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	f(i, 1, t + 1){
		scanf("%d", &n);
		f(i, 0, 10) l[i] = 0;
		c = 0;
		f(j, 1, 2000){
			int x = j * n;
			while(x){
				if(!l[x%10]){
					c++;
					l[x%10]++;
				}if(c == 10){
					ans = j * n;
					break;
				}
				x /= 10;
			}
			if(c == 10) break;
		}
		printf("Case #%d: ", i);
		if(c != 10) printf("INSOMNIA\n");
		else printf("%d\n", ans);
	}
	scanf("\n");
}
