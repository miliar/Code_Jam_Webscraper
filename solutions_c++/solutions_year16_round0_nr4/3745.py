#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long int lli;
typedef pair<lli, lli> ii;
const int MAXN = 10010, MAXL = 1000010;

int n, flips;
lli k, c, s;

int main() {
	//freopen("D-small-attempt0.in", "r", stdin);
	//freopen("output-small.txt", "w", stdout); 

	int t;
	scanf("%d", &t);

	for(int test=1; test<=t; test++) {
		printf("Case #%d:", test);

		scanf("%lld %lld %lld", &k, &c, &s);
		lli jump = 1;
		for(lli i=1; i<c; i++) {
			jump *= k;
		}
		for(lli i=0; i<k; i++) {
			printf(" %lld", 1ll+jump*i);
		}
		printf("\n");
	}
}
