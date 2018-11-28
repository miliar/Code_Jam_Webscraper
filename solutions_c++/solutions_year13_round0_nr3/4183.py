#include <cstdio>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
 
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define sz size()
#define sqr(x) (x) * (x)
#define all(x) (x).begin(), (x).end()

vector<long long> pals;

bool ispal(long long n) {
	long long m = 0, n1 = n;
	while(n) {
		m = m * 10 + n % 10;
		n /= 10;
	}
	return (n1 - m == 0);
}

void init() {
	for(long long i = 1; i <= 10000000; i++) {
		if(ispal(i) && ispal(i * i))
			pals.pb(i * i);
	}
}
void solve() {
	long long l, r;
	int cnt = 0;
	scanf("%lld%lld", &l, &r);
	for(int i = 0; i < pals.sz; i++) {
		if(pals[i] >= l && pals[i] <= r) cnt++;
	}

	printf("%d\n", cnt);
}
void OJ() {
    int t = 0;
    scanf("%d", &t);
	init();
	//cout << pals.sz << endl;
    for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
        solve();
    }
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    OJ();
    
    return 0;
}