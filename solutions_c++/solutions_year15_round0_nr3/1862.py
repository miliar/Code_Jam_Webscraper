#include "iostream"
#include "cstring"
#include "cstdio"
#include "algorithm"
using namespace std;
const int N = 10100;
char s[N];
int dp[N];
int dic[128];
int d[5][5];
int ab(int x)
{
	return x > 0 ? x: -x;
}
int gao(int x, int y){
	if(x == 1) return y;
	if(x == -1) return -y;
	int op = x * y > 0 ? 1 : -1;
	x = ab(x);
	y = ab(y);
	if(x == 2){
		if(y == 2) return -1 * op;
		if(y == 3) return 4 * op;
		if(y == 4) return -3 * op;
	}
	if(x == 3){
		if(y == 2) return -4 * op;
		if(y == 3) return -1 * op;
		if(y == 4) return 2 * op;
	}
	if(x == 4){
		if(y == 2) return 3 * op;
		if(y == 3) return -2 * op;
		if(y == 4) return -1 * op;
	}
	return -1;
}
int main(void)
{
	dic['i'] = 2;
	dic['j'] = 3;
	dic['k'] = 4;
	int T;
	int g = 0;
	scanf("%d",&T);
	int n;
	long long x;
	while(T --){
		printf("Case #%d: ", ++g);
		cin >> n >> x;
		scanf("%s", s);
		int l = n * x;
		int now = 1;
		int mark = -1;
		for(int i = 0; i < l; ++ i){
			int idx = dic[s[i % n]];
			now = gao(now, idx);
			if(now == 2){
				mark = i + 1;
				break;
			}
		}
		if(mark == -1){
			puts("NO");
			continue;
		}
		int flag = -1;
		now = 1;
		for(int i = mark; i < l ; ++ i){
			int idx = dic[s[i % n]];
			now = gao(now, idx);
			if(now == 3){
				flag = i + 1;
				break;
			}
		}
		if(flag == -1){
			puts("NO");
			continue;
		}
		now = 1;
		for(int i = flag; i < l; ++ i){
			int idx = dic[s[i % n]];
			now = gao(now, idx);
		}
		if(now == 4){
			puts("YES");
		}else{
			puts("NO");
		}
	}

	return 0;
}