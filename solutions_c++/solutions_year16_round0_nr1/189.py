#include <cstdio>
#include <cstring>

const int MAXD = 10;

int tot, cnt[10];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		int n;
		scanf("%d", &n);
		if (n == 0)
			puts("INSOMNIA");
		else{
			int m = 0;
			tot = 10;
			memset(cnt, 0, sizeof(cnt));
			while (tot){
				for (int t = m += n; t; t /= 10)
					tot -= !(cnt[t % 10]++);
			}
			printf("%d\n", m);
		}
	}
	return 0;
}
