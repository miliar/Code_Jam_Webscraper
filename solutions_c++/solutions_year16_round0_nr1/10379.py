#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <string.h>
#include <algorithm>
#define N 1000
#define INF 0x3f3f3f

using namespace std;

const int MOD = 1e9+7, maxn = 1e5+5;
int t, f[20];
long long n, m, in;

int max(int x, int y) {	return x>y ? x:y;}
int min(int x, int y) {	return x<y ? x:y;}
void swap(int &x, int &y) { int temp = x; x = y; y = temp;}
void work() {
	if (n == 0) {
		printf("INSOMNIA\n");
		return;
	}
	memset(f, 0, sizeof(f));
	int len = 0, sum = 0;
	m = n;
	in = n;
	while (m > 0) {
		int temp = m % 10;
		m /= 10;
		if (f[temp] == 0) {
			sum++;
			f[temp] = 1;
		}
	}
	int tot = 0;
	while (sum < 10) {
		n += in;
//		cout<<n<<' '<<sum<<endl;
		m = n;
		while (m > 0) {
			int temp = m % 10;
			m /= 10;
			if (f[temp] == 0) {
				sum++;
				f[temp] = 1;
			}
		}		
	}
	if (sum == 10) printf("%d\n", n);
}
int main() {
//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int p = 1; p <= t; p++) {
		scanf("%d", &n);
		printf("Case #%d: ", p);
		work();
	}
	return 0;
}
