#include<cstdio>
#include<iostream> 
#include<cmath>
using namespace std;
int T;
int x;
int ans = 0;
#define N 1000000
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	int t = 0;
	while (T --){
		ans = 0;
		int x0;
		scanf("%d", &x);
		x0 = x;
		for (int i = 1; i <= N; i ++){
			if (ans == 1023){
				printf("Case #%d: %d\n",++t, x - x0);
				break;
			}
			int tmp = x;
			while (tmp){
				ans |= (1 << (tmp % 10));
				tmp /= 10;
			}
			x += x0;
		}
		if (ans != 1023){
			printf("Case #%d: INSOMNIA\n", ++t);
		}
	}
}
