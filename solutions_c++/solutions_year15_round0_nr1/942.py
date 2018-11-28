
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long i8;

int ntc$, cas$;

int solve() {
	int n;
	char row[1005];
	scanf("%d %s",&n,row);
	
	int up=0, tt=0;
	for (int s=0; s<=n; s++) {
		int h=row[s]-'0';
		if (h && up<s)
			up=s;
		up+=h;
		tt+=h;
	}
	return up-tt;
}

main() {
	scanf("%d", &ntc$);
	for (int cas$=1; cas$<=ntc$; cas$++) {
		printf("Case #%d: %d\n", cas$, solve());
	}
}
