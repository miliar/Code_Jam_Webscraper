#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <deque>
#include <cctype>
#include <list>
#include <queue>
#include <map>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int t;

bool ispal(int x) {
	int arr[1000] = {0};
	int pos = 0;
	while ( x > 0 ) {
		arr[pos++] = x % 10; x /= 10;
	}
	for ( int i = 0 ; i < pos / 2 ; ++i )
		if ( arr[i] != arr[pos - i - 1] )
			return false;
	return true;
}

int solve(int a, int b) {
	int answer = 0;
	for ( int i = a ; i <= b ; ++i ) {
		int sq = sqrt((double)i);
		if ( ispal(i) && ispal(sq) && sq * sq == i )
			++answer;
	}
	return answer;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
#endif

	scanf("%d", &t);
	for ( int i = 0 ; i < t ; ++i ) {
		int a, b; scanf("%d%d", &a, &b);
		printf("Case #%d: %d\n", i + 1, solve(a, b));
	}

	return 0;
}