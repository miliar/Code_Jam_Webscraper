#include <cstdio>

const int N = 1002;
int sum , ans , n;
char st[N];

void Work(){
	scanf("%d %s" , &n , st);
	sum = st[0] - '0';
	ans = 0;
	for(int i = 1; i <= n; i ++){
		if(sum < i){
			ans += i - sum;
			sum = i;
		}
		sum += st[i] - '0';
	}
	printf("%d\n" , ans);
}

int main(){
	//freopen("a2.in" , "r" , stdin);
	//freopen("a.out" , "w" , stdout);
	
	int T;
	scanf("%d" , &T);
	for(int i = 1; i <= T; i ++){
		printf("Case #%d: " , i);
		Work();
	}
	
	return 0;
}