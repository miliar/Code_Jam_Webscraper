#define MAX(a,b) ((a) > (b))?(a):(b)
#include <cstdio>
#include <cstdlib>

int main(){
	char testnum_s[10] = {0}, lastpos_s[10] = {0}, value_s[1005] = {0};
	int sum = 0, i = 0, j = 0, testnum = 0, lastpos = 0, value = 0, deficit = 0;
	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);
	scanf("%s", testnum_s);
	testnum = atoi(testnum_s);
	for(i = 0; i < testnum; ++i){
		scanf("%s", lastpos_s);
		lastpos = atoi(lastpos_s);
		sum = deficit = 0;
		scanf("%s", value_s);
		sum = value = value_s[0] - '0';
		for(j = 1; j <= lastpos; ++j){
			/*
			if(j > sum + deficit){
				++deficit;
			}
			*/
			if(j > sum){
				deficit += j-sum;
				sum = j;
			}
			value = value_s[j] - '0';
			sum += value;
		}
		printf("Case #%d: %d\n", i+1, deficit);
	}
	return 0;
}
