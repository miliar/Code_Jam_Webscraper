#include <cstdio>
#include <cstring>
#include <cstdlib>

#define rep(a,b,c) for (int a=b, _c=c; a<_c; ++a)

void solve(int);
int main() {
	int T;
	scanf("%d", &T);
	for (int x=1; x<=T; ++x) solve(x);
	return 0;
}

int sz;
char i[128];
void solve(int tc)
{
	int ans=0;
	scanf("%s", i);
	sz = strlen(i);
	rep(x,1,sz)
		if (i[x]!=i[x-1]) ++ans;
	if (i[sz-1]=='-') ++ans;
	printf("Case #%d: %d\n", tc, ans);
}