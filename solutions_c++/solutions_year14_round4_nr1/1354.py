/*
 * Author    : ben
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <functional>
#include <numeric>
#include <cctype>
using namespace std;
const int MAXN = 10009;
int data[MAXN];

int work() {
	int N, X, ret = 0;
	scanf("%d%d", &N, &X);
	for(int i = 0; i < N; i++) {
		scanf("%d", &data[i]);
	}
	sort(data, data + N);
	int s = 0, e = N - 1;
	while(s <= e) {
		if(data[e] + data[s] <= X) {
			s++;
		}
		e--;
		ret++;
	}
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		printf("Case #%d: %d\n", t, work());
	}
	return 0;
}


