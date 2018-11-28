#include<cstdio>
#include<set>
#include<vector>
#include<algorithm>
#include<string.h>
using namespace std;

#define MAX_V 5000
#define INF 100000

char people[1002];
int len;

int main() {
	int tests;
	scanf("%d",&tests);
	for(int test = 1; test <= tests; test++) {
		scanf("%d",&len);
		scanf("%s",&people);
		int ret = 0;
		int sum = 0;
		for (int i = 0; i <= len; i++) {
			if(i > sum && (people[i] - '0' > 0)) {
				ret += i - sum;
				sum = i + people[i] - '0';
			} else {
				sum += people[i] - '0';
			}
		}

		printf("Case #%d: %d\n", test, ret);
	}
	return 0;
}