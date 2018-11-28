#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
const int N = 1010;
char s[N];
int main(void)
{
	int T;
	int g = 0;
	scanf("%d",&T);
	while(T --){
		int n;
		cin >> n >> s;
		int sum = 0;
		int ans = 0;
		for(int i = 0; i <= n; ++ i){
			if(sum >= i){
				sum += s[i] - '0';
			}else{
				ans += i - sum;
				sum = i + s[i] - '0';

			}
		}
		printf("Case #%d: %d\n", ++g, ans);
	}
	return 0;
}