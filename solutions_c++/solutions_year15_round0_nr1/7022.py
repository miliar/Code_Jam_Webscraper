#include <cmath>
#include <cstdio>
#include <algorithm>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;
typedef long long i64;

int doIt(int n, char *k) {
	int *list = (int*)malloc(sizeof(int) * n);
	int cnt = 0, result = 0, sum = 0;
	char tmp[2];

	for(cnt = 0; cnt <= n; cnt++){
		tmp[0] = k[cnt];
		tmp[1] = '\0';
		list[cnt] = atoi(tmp);
	}

	result = 0; sum = 0;
	for(cnt = 0; cnt <= n; cnt++){
		sum += list[cnt];
		if(sum < cnt + 1){
			//result = cnt + 1 - sum;
			result++;
			sum++;
		}
	}
	//free(list);
	return result;
}

int main() {
	int T; scanf("%d", &T);
	int n;
	char *k = (char*)malloc(sizeof(char) * 1200);
	for (int Ti = 1; Ti <= T; ++Ti) {
		scanf("%d %s", &n, k);
		printf("Case #%d: %d\n", Ti, doIt(n, k));
	}
	return 0;
}
