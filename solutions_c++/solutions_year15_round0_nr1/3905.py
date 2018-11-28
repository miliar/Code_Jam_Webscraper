#include<cstdio>
#include<algorithm>

using namespace std;

#define N 10000
int n, C, caso;
char s[N + 5];

void doCase(){
	scanf("%d", &n);
	scanf("%s", s);

	int cnt = 0;
	int ans = 0;
	for(int i = 0; i <= n; ++i){
		int d = s[i] - '0'; 
		int need = max(0, i - cnt);
		cnt += d;
		ans = max(ans, need);
	}

	printf("Case #%d: %d\n", ++caso, ans);
}
int main(){
	caso = 0;
	scanf("%d", &C);
	for(int i = 0; i < C; ++i)doCase();
}
