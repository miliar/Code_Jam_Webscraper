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
#include <iostream>
#include <algorithm>
#define ff first
#define ss second
#define LL long long
#define pb push_back
#define mp make_pair
#define sqr(x) ((x) * (x))
#define PI 3.1415926535897
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("AA-large.out", "w", stdout);
	string a;
	int t, n, sum, ans;
	scanf("%d", &t);
	for (int j = 1; j <= t; j++) {
		scanf("%d", &n); ans = 0;
		cin >> a; sum = a[0] - '0';
		for (int i = 1; i <= n; i++) {
			if (i > sum) {
				ans += i - sum;
				sum = i + (a[i] - '0');
			}
			else sum += (a[i] - '0');
		}
		printf("Case #%d: %d\n", j, ans);
	}
	return 0;
}

