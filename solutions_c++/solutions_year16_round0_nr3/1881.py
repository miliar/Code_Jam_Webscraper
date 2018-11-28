#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<set>
#include<string>
#include<map>

using namespace std;
#define INF 0x3f3f3f3f

char buff[1000];

int num[40];
int div[40];

typedef long long LL;

LL pow[40][40];
LL pow31[40][40];

bool check(int n){
	for(int i = 2;i <= 10;++i){
		LL now = 0;
		for(int j = 0;j < n;++j)
			now += num[j] * pow[i][j];
		bool is_prime = true;
		for(LL j = 2;j * j <= now;++j){
			if(j > 10)
				break;
			if((now + pow31[i][j]) % j == 0){
				is_prime = false;
				div[i] = j;
				break;
			}
		}
		if(is_prime)
			return false;
	}
	return true;
}

void solve(int n,int J){
	num[0] = 1;
	num[n - 1] = 1;
	int cnt = 0;
	for(int i = 0;i < (1 << (n - 2));++i){
		for(int j = 0;j < n - 2;++j){
			if((i >> j) & 1)
				num[j + 1] = 1;
			else
				num[j + 1] = 0;
		}
		if(check(n)){
			++cnt;
			printf("1");
			for(int i = 0;i < 15;++i)
				printf("0");
			for(int i = n - 1;i >= 0;--i)
				printf("%d",num[i]);
			for(int i = 2;i <= 10;++i)
				printf(" %d",div[i]);
			printf("\n");
			if(cnt == J)
				break;
		}
	}
	if(cnt < J)
		printf("not enough\n");
//	printf("cnt %d\n",cnt);
}

int main(){
	for(int i = 2;i <= 10;++i)
		pow[i][0] = 1;
	for(int i = 2;i <= 10;++i)
		for(int j = 1;j <= 16;++j)
			pow[i][j] = pow[i][j - 1] * i;
	for(int i = 2;i <= 10;++i)
		for(int j = 2;j < 10;++j){
			pow31[i][j] = 1;
			for(int k = 0;k < 31;++k)
				pow31[i][j] = pow31[i][j] * i % j;
		}
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		int n,J;
		scanf("%d%d",&n,&J);
		n = 16;
		printf("Case #%d:\n",cas);
		solve(n,J);
	}
	return 0;
}

