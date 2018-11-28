#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;

int test, n;
char s[105];

void check() {
	while (n && s[n - 1] == '+') n--; 
}

void rev(int x) {
	if (s[x] == '-') s[x] = '+';
	else if (s[x] == '+') s[x] = '-'; 
}

void flip(int x) {
	FOR(i, 0, (x/2) + 1) {
		swap(s[i], s[x - i]);
		rev(i);
		if (x - i != i) rev(x - i);
	}
}

void solve(int tc) {
	scanf("%s", s);
	n = strlen(s);
	printf("Case #%d: ", tc + 1);
	
	check();
	
	int steps = 0; 
	while (n > 0) {
		
		int p = 0;
		for (; p + 1 < n && s[p + 1] == s[p]; p++);
		
		if (s[p] == '+') {
			flip(p);
			steps++;
		}
		
		flip(n - 1);
		steps++;
		
		check();
	}
	
	printf("%d\n", steps);
}

int main(){
	scanf("%d", &test);
	FOR(tc, 0, test) solve(tc);
	return 0;
}
