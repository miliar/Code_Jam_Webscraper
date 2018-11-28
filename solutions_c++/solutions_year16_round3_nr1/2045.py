#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <iostream>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

int N;
int arr[30];

int total() {
	int sum = 0;
	REP(i, 0, N) {
		sum += arr[i];
	}
	return sum;
}

bool checkMaj() {
	int t = total();
	if(t == 0) return false;

	int m = 0;
	REP(i, 0, N) {
		if(arr[i] > m) m = arr[i];
	}
	if(m > t/2) return true;

	return false;
}

bool p1(int p) {
	int m = -1, mi;
	REP(i, 0, N) {
		if(arr[i] > m) {
			m = arr[i];
			mi = i;
		}
	}
	arr[mi] -= p;
	if(checkMaj()) {
		arr[mi] += p;
		return false;
	}

	printf("%c", 'A'+mi);
	return true;
}

bool p2() {
	int m1 = 0, m2 = 0, mi1, mi2;
	int t = total();
	if(t <= 1) return false;

	REP(i, 0, N) {
		if(arr[i] > m1) {
			m2 = m1;
			mi2 = mi1;
			m1 = arr[i];
			mi1 = i;
		} else if(arr[i] > m2) {
			m2 = arr[i];
			mi2 = i;
		}
	}

	arr[mi1] -= 1;	
	arr[mi2] -= 1;
	if(checkMaj()) {
		arr[mi1] += 1;
		arr[mi2] += 1;
		return false;
	}

	printf("%c%c", 'A'+mi1, 'A'+mi2);
	return true;
}

void solve() {
	int f = true;
	int t;
	while((t=total()) > 0) {
		if(f) {
			f = false;
		} else {
			printf(" ");
		}

		if(p2()) continue;
		if(p1(2)) continue;
		if(p1(1)) continue;
	}
	printf("\n");
}

void docase() {
	scanf("%d", &N);
	REP(i, 0, 30) arr[i] = 0;

	REP(i, 0, N) {
		scanf("%d", &arr[i]);
	}

	solve();
}

int main() {
	int T;
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		printf("Case #%d: ", test+1);
		docase();
	}
	return 0;
}
