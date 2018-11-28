#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <string>
#include <climits>
#define ull unsigned long long
#define ll long long
#define ul unsigned long
#define vi vector<int>
#define vll vector<long long>
#define pb push_back
#define pii pair<int, int>
#define pll pair<long long, long long>
#define mp make_pair
#define pq priority_queue

using namespace std;

ll n;

void process(ll n) {
	ll mult = 0;
	bool dig[10];
	memset(dig, 0, sizeof dig);
	do {
		mult += n;
		ll temp = mult;
		while(temp > 0) {
			dig[temp % 10ll] = 1;
			temp /= 10ll;
		}
	} while(!(dig[0] && dig[1] && dig[2] && dig[3] && dig[4] && dig[5] && dig[6] && dig[7] && dig[8] && dig[9]));
	printf("%lld\n", mult);
}

int main() {
	int tc;
	scanf("%d", &tc);
	
	int itc = 0;
	while(tc--) {
		scanf("%lld", &n);
		if(n == 0ll) {
			printf("Case #%d: INSOMNIA\n", ++itc);
		} else {
			printf("Case #%d: ", ++itc);
			process(n);
		}
	}
	return 0;
}
