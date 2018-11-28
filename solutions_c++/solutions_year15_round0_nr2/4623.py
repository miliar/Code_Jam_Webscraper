#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 7;
int T , ans , n;
int a[N];

void Dfs(int x , int t){
	if(x > n){
		int tmax = a[1];
		for(int i = 1; i <= n; i ++) tmax = max(tmax , a[i]);
		ans = min(ans , tmax + t);
		return;
	}
	for(int i = 1; i <= a[x]; i ++) if (a[x] - i + 1 >= a[x] / i){
		int tt = a[x];
		a[x] = (a[x] / i) + (a[x] % i != 0);
		Dfs(x + 1 , t + i - 1);
		a[x] = tt;
	}
}

void Work(){
	scanf("%d" , &n);
	for(int i = 1; i <= n; i ++) scanf("%d" , &a[i]);
	ans = 10;
	Dfs(1 , 0);
	printf("%d\n" , ans);
}

int main(){
	//freopen("b1.in" , "r" , stdin);
	//freopen("b.out" , "w" , stdout);
	
	scanf("%d" , &T);
	for(int i = 1; i <= T; i ++){
		printf("Case #%d: " , i);
		Work();
	}
	
	return 0;
}