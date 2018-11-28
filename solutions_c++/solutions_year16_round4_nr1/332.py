#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
using namespace std;
int S[8195];
int n;
bool test(int r, int p, int s, const char *ch)
{
	if (r == 0) return 0;
	-- r;
	S[1] = 0;
	for (int i = 1; i < (1 << n); ++ i)
	{
		S[i * 2] = S[i];
		S[i * 2 + 1] = (S[i] + 2) % 3;
		if (S[i * 2 + 1] == 0) -- r;
		if (S[i * 2 + 1] == 1) -- p;
		if (S[i * 2 + 1] == 2) -- s;
		if (ch[S[i * 2 + 1]] < ch[S[i * 2]]) swap(S[i * 2], S[i * 2 + 1]);
		if (r < 0 || p < 0 || s < 0) return 0;
	}
	for (int i = 1 << n; i < (1 << n) * 2; ++ i) S[i] = ch[S[i]];
	return 1;
}
void mysort(int n, int l)
{
	if (n < 0) return;
	int x = l + (1 << n);
	mysort(n - 1, l);
	mysort(n - 1, x);
	for (int i = 0; i < (1 << n); ++ i)
	{
		if (S[l + i] != S[x + i])
		{
			if (S[l + i] > S[x + i])
			{
				for (int j = 0; j < (1 << n); ++ j) swap(S[l + j], S[x + j]);
			}
			break;
		}
	}
}
string print(const char *s)
{
	string ans;
	for (int i = 1 << n; i < (1 << n) * 2; ++ i) ans += S[i];
	return ans;
}
int main()
{
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --)
	{
		int r, p, s;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		printf("Case #%d: ", ++ zzz);
		string ans = "";
		if (test(r, p, s, "RPS"))
		{
			mysort(n - 1, 1 << n);
			string t = print("RPS");
			if (ans == "" || ans > t) ans = t;
		}
		if (test(p, s, r, "PSR"))
		{
			mysort(n - 1, 1 << n);
			string t = print("PSR");
			if (ans == "" || ans > t) ans = t;
		}
		if (test(s, r, p, "SRP"))
		{
			mysort(n - 1, 1 << n);
			string t = print("SRP");
			if (ans == "" || ans > t) ans = t;
		}
		if (ans == "")
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			cout << ans;
		}
		puts("");
	}
}

