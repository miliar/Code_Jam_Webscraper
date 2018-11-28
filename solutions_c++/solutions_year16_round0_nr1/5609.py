#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long int lli;
typedef pair<lli, lli> ii;
const int MAXN = 10010, MAXL = 1000010;

int n;
bool seen[10];

int countSeen();

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("output-large.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for(int test=1; test<=t; test++) {
		scanf("%d", &n);

		memset(seen, false, sizeof(seen));
		for(int i=1; i<=1000; i++) {
			int aux = n*i;
			while(aux) {
				seen[aux%10] = true;
				aux /= 10;
			}
			if(countSeen() == 10) {
				n *= i;
				break;
			}
		}
		if(countSeen() < 10) {
			n = 0;
		}

		printf("Case #%d: ", test);
		if(n) printf("%d\n", n);
		else printf("INSOMNIA\n");
	}
}

int countSeen() {
	int ans = 0;
	for(int i=0; i<10; i++) ans += seen[i];
	return ans;
}
