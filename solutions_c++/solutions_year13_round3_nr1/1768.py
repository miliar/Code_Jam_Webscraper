#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <memory.h>
#include <set>

using namespace std;

int tc = 1, len, n;
bool d[101];
char t_str[101];
string str;
int ans(0);

bool cc(char s) {
	if( s == 'a' || s == 'i' || s == 'o' || s == 'u' || s == 'e' ) return 1;
	return 0;
}

void solve() {
	memset(d, 0, sizeof d);
	memset(t_str, 0, sizeof t_str);
	scanf("%s", t_str); 
	scanf("%d", &n);
	str = t_str;
	len = strlen(t_str);
	int last = 0;
	for(int i=0; i<len; i++) d[i] = cc(t_str[i]);
	for(int i=0; i<len; i++) {
		bool ok(0);
		for(int j=0; j<n; j++) if( d[i+j] == true ) {
			ok = true;
			break;
		}
		if( ok ) continue;	
		for(int j=last; j<=i; j++)
			for(int k=i+n-j; k<=len-j; k++) 
				ans++;
		last = i+1;
	}
	printf("Case #%d: %d\n", tc++, ans);
	ans = 0;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int TC;
	scanf("%d", &TC);
	while(TC-- > 0) solve();
}
