#include "iostream"
#include "cstring"
#include "cstdio"
#include "algorithm"
using namespace std;
const int N = 1010;
int a[N];
int check(int k, int n)
{
	int sum = 0;
	for(int i = 1; i <= n; ++ i){
		if(a[i] > k){
			sum += (a[i] + k - 1) / k - 1;
		}
	}
	return sum + k;
}
int main(void)
{
	int T;
	int g = 0;
	scanf("%d",&T);
	int n;
	while(T --){
		scanf("%d", &n);
		for(int i = 1; i <= n; ++ i){
			cin >> a[i];
		}
		sort(a + 1, a + 1 + n);
		int ans = 1010;
		for(int i = 1; i <= 1000; ++ i){
			ans = min(ans, check(i, n));
		}
		printf("Case #%d: %d\n", ++g, ans);
	}
	return 0;
}