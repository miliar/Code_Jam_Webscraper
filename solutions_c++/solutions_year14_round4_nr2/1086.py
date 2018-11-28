#include "iostream"
#include "cstring"
#include "cstdio"
#include "string"
#include "algorithm"
using namespace std;
int a[20];
int t[20];
int c[20];
int check(int n)
{
	for(int i = 0; i < n; ++ i){
		int flag = 1;
		for(int j = 0; j < i - 1; ++ j){
			if(c[j] > c[j + 1]){
				flag = 0;
				break;
			}
		}
		for(int j = i; j < n - 1; ++ j){
			if(c[j] < c[j + 1]){
				flag = 0;
				break;
			}
		}
		if(flag) return 1;
	}
	return 0;
}
int gao(int n)
{
	int sum = 0;
	for(int i = 1; i < n; ++ i){
		for(int j = 0; j < i; ++ j){
			if(t[j] > t[i]){
				sum ++;
			}
		}
	}
	return sum;
}
int main(void)
{
	int T, n;
	scanf("%d", &T);
	int g = 0;
	while(T --){
		scanf("%d", &n);
		for(int i = 0; i < n; ++ i){
			scanf("%d", &a[i]);
		}
		for(int i = 0; i < n; ++ i){
			t[i] = i;
		}
		int ans = 1000000;
		do{
			for(int i = 0; i < n; ++ i){
				c[t[i]] = a[i];
			}
			if(check(n)){		
				ans = min(ans, gao(n));
			}
		}while(next_permutation(t, t + n));
		printf("Case #%d: %d\n", ++ g, ans);
	}
	return 0;
}