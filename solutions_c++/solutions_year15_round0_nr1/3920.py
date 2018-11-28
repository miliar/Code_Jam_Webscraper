#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     (A).begin(), (A).end()
typedef long long ll;

int N, smax;
char D[1010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d%s", &smax, D);
		int ans = 0, cur = D[0]-'0';
		for (int i = 1; i <= smax; i++) {
			if (cur <= i) {
				ans += i-cur;
				cur += i-cur;
			}
			cur += D[i]-'0';
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
