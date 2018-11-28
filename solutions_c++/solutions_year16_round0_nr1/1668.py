#include <bits/stdc++.h>
using namespace std;
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<ii, ii>
#define vvi vector<vi>
#define MAX 1000000
#define MAXN 200005
#define MAXE 100005
#define INF 10000000
#define MOD 1000000007
#define FOR(x,n) for(int x = 0; x < n; x++)
#define FOR1e(x,n) for(int x = 1; x <= n; x++)

bool seen[10];
bool checkseen() {
	FOR(x, 10) if(!seen[x]) return true;
	return false;
}
int main() {
	int c, n, tmp, ult;
	scanf("%d", &c);
	FOR1e(caso, c) {
		printf("Case #%d: ", caso);
		scanf("%d", &n);
		if(n == 0) {
			printf("INSOMNIA\n"); continue;
		}
		FOR(x, 10) seen[x] = false;
		
		ult = 0;
		while(checkseen()) {
			ult += n;
			tmp = ult;
			while(tmp > 0) {
				seen[tmp%10] = true;
				tmp /= 10;
			}
		}
		printf("%d\n", ult);
	}
}