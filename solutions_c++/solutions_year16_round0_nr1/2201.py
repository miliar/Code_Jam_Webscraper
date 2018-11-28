#include <string>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <queue>

using namespace std;
#pragma warning(disable:4996)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define rep(i,n) for (int i=0; i<n; i++)
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define ll long long
#define N 1000

int main() {
	freopen("try.in", "r", stdin);
	freopen("try.out", "w", stdout);

	int n, t;
	scanf("%d", &t);
	rep(tt, t) 
	{
		scanf("%d", &n);
		bool a[10] = { 0 };
		int num = 0, w = 0;
		if (n > 0)
		FOR(i, 1, 100) {
			for (int ww = w = i * n; ww; ww /= 10) 
				if (!a[ww % 10]) num++, a[ww % 10] = true;
			if (num == 10) break;
		}
		printf("Case #%d: ", tt + 1);
		if (num == 10) printf("%d\n", w); else printf("INSOMNIA\n");
	}
}