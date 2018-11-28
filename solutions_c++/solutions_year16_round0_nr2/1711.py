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

char palavra[1000];

int main() {
	int c, ans, n, v;
	scanf("%d", &c);
	FOR1e(caso, c) {
		printf("Case #%d: ", caso);
		scanf(" %s", palavra);
		
		n = strlen(palavra);
		ans = 0;

		for(int i = n-1; i >= 0;) {
			if(palavra[i] == '+') {
				while(i >= 0 && palavra[i] == '+') i--;
				if(ans != 0) ans++;
			}
			if(palavra[i] == '-') {
				while(i >= 0 && palavra[i] == '-') i--;
				ans++;
			}
		}

		printf("%d\n", ans);
	}
}