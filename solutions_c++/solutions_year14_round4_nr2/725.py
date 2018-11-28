
#include <cstdio>

int min(int a, int b){
	if(a < b) return a;
	return b;
}

int main(){
	
	int testcase; scanf("%d", &testcase);
	int n;
	int s[1000];
	int a, b;
	int sum;

	for(int t=1; t<=testcase; ++t){
		scanf("%d", &n);
		for(int i=0; i<n; ++i){
			scanf("%d", &s[i]);
		}
		sum = 0;
		for(int i=0; i<n; ++i){
			a = b = 0;
			for(int j=0; j<i; ++j){
				if(s[i] < s[j]){
					++ a;
				}
			}
			for(int j=i+1; j<n; ++j){
				if(s[i] < s[j]){
					++ b;
				}
			}
			sum += min(a, b);
		}
		printf("Case #%d: %d\n", t, sum);
	}
	return 0;
}
