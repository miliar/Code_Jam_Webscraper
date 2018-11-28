#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int t,n,i,j;
bool flag[15];

bool check(int s){
	long long now = (long long)s * n;
	while(now){
		flag[now % 10] = 1;
		now /= 10;
	}
	bool ok = 1;
	for(int k = 0; k < 10; k++)
	ok &= flag[k];
	return ok;
}

int main(){
	scanf("%d", &t);
	int testcase = 0;
	
	while(++testcase <= t){
		memset(flag, 0, sizeof(flag));
		
		scanf("%d", &n);
		printf("Case #%d: ", testcase);
		
		if(n == 0){
			printf("INSOMNIA\n");
			continue;
		}
		
		for(i = 1; ; i++){
			if(check(i)){
				printf("%lld\n", (long long)i * n);
				break;
			}
		}
		
	}
}

