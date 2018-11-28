#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ff first
#define ss second
#define LL long long
#define pb push_back
#define mp make_pair
#define sqr(x) ((x) * (x))
#define PI 3.1415926535897932384626433832795
using namespace std;

int main() {
	int a, b, k, i, l, t, tc = 1, ans;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		scanf("%d%d%d", &a, &b, &k);
		ans = 0;
		for(i = 0; i < a; i++) {
			for(l = 0; l < b; l++) {
				if((i&l) < k) ans++;
			}
		}
		printf("Case #%d: %d\n", tc++, ans);
	}
	return 0;
}
