#include <cstdio>

using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++) {
		int sm, sum = 0, res = 0;
		scanf("%d", &sm);
		for(int j = 0; j <= sm; j++) {
			char ch;
			scanf(" %c", &ch);
			int count = ch - '0';
			if(count > 0) {
				if(sum < j) {
					res += j - sum;
					sum = j;
				}
				sum += count;
			}
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}