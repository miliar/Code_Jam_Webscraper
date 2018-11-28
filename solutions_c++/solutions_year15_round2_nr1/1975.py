#include <iostream>
#include <queue>
#include<cstdio>
#include<vector>

#define MAX 1111111
using namespace std;

int arr[MAX];

int rev(int x) {
	int rev = 0;
	while (x > 0) {
		rev = rev * 10 + (x % 10);
		x /= 10;
	}
	return rev;
}

queue<int> ns;
int main() {
	int a, b, c;
	arr[1] = 1;
	ns.push(1);
	while (!ns.empty()) {
		int x = ns.front();
		ns.pop();
		if (x + 1 < MAX and arr[x + 1] == 0) {
			arr[x + 1] = arr[x] + 1;
			ns.push(x + 1);
		}
		if (rev(x) < MAX and arr[rev(x)] == 0) {
			arr[rev(x)] = arr[x] + 1;
			ns.push(rev(x));
		}
	}
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		long long n;
		cin >> n;
		printf("Case #%d: %d\n", i, arr[n]);
	}
}
