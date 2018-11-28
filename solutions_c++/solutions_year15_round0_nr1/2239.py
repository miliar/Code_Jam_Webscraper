#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		int level;
		scanf("%d ", &level);
		char num;
		int sum = 0;
		int ans = 0;
		for (int i = 0; i <= level; i++){
			num = getchar();
			if (sum >= i){
				sum += num - '0';
			}else {
				ans += i - sum;
				sum = i + (num - '0');
			}
		}
		printf("Case #%d: ", t);
		printf("%d\n",ans);
	}
	return 0;
}
