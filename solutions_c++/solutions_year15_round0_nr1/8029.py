#include<cstdio>
#include<cstdlib>

int t, n;
char m[1005];

int fm(int a, char* q){
	int u = 0, y = 0;
	for(int i = 0 ; i <= a ; i++){
		if(u < i){
			y += i - u;
			u += i - u;
		}
		u += m[i] - '0';
	}
	return y;
}

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0 ; i < t ; i++){
		scanf("%d %s", &n, &m);
		int k = fm(n, m);
		printf("Case #%d: %d\n", i + 1, k);
	}
	return 0;
}
