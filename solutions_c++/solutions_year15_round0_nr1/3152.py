#include <cstdio>
#include <cstring>
#define ARRSIZE 1111

char s[ARRSIZE];
int lim[ARRSIZE];
int slove( int Smax, char s[]){
	for (int i = 0; i <= Smax; i++)
		lim[i] = s[i] - '0';
	int ans = 0, now = 0;
	for (int i = 0; i <= Smax; i++){
		if(now<i){
			ans += i - now;
			now = i;
		}
		now += lim[i];
	}
	return ans;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int caseT = 1; caseT <= T; caseT++){
		int Smax;
		scanf( "%d %s", &Smax, s);
		printf("Case #%d: %d\n", caseT, slove( Smax, s));
	}
	return 0;
}