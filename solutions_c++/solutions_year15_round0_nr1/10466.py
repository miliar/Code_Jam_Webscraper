#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <iostream>

using namespace std;

int TC;
int N;
char audience[1024];
 
int main() {
	scanf("%d", &TC);
	for(int tc = 1; tc <= TC; ++tc) {
		scanf("%d %s", &N, audience);
 
		int friends = 0;
		int total = 0;
		for(int i = 0; i <= N; ++i) {
			if(total >= i) {
				total += audience[i] - '0';
			} else if(audience[i] > '0') {
				friends += i - total;
				total += friends + audience[i] - '0';
			}
		}
 
		printf("Case #%d: %d\n", tc, friends);
	}
	return 0;
}

