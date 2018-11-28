#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w",stdout);
	int t;
	scanf("%d", &t);
	for(int j = 1; j <= t; j++){
		int n;
		scanf("%d", &n);
		int cur;
		scanf("%d", &cur);
		int one = 0, largest = 0, ms[1005];
		ms[0] = cur;
		for(int i = 1; i < n; i++){
			int tmp;
			scanf("%d", &tmp);
			ms[i] = tmp;
			if(tmp < cur){
				one += cur - tmp;
				largest = max(largest, cur-tmp);
			}
			cur = tmp;
		}
		int two = 0;
		for(int i = 0; i < n-1; i++){
			two += min(largest, ms[i]);
		}
		printf("Case #%d: %d %d\n", j, one, two);
	}
	return 0;
}

