#include <stdio.h>
#include <string.h>
#include <string>
#include <unordered_map>
#include <bitset>
#include <algorithm>

using namespace std;

const int MAXN = 20;
int n;
char buf[100000];
unordered_map<string, int> id;
int cnt;
bitset<2200> S[MAXN];
int ans;

int getid(string s)
{
	if (id.find(s) != id.end()) return id[s];
	return id[s] = cnt++;
}

void init()
{
	cnt = 0;
	id.clear();
	scanf("%d", &n);
	gets(buf);
	for (int i = 0; i < n; ++i) {
		S[i] = 0;
		gets(buf);
		char *s = strtok(buf, " ");
		while (s) {
			S[i].set(getid(s));
			s = strtok(NULL, " ");
		}
	}
}

int calc(int mask)
{
	bitset<2200> M[2];
	for (int i = 0; i < n; ++i) {
		M[mask>>i&1] |= S[i];
	}
	return (M[0]&M[1]).count();
}

void solve()
{
	ans = cnt;
	for (int i = 0; i < 1<<(n-2); ++i) {
		ans = min(ans, calc((i<<2)|1));
	}
}

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int cas = 1; cas <= dat; ++cas) {
		init();
		solve();
		printf("Case #%d: %d\n", cas, ans);
	}
}
