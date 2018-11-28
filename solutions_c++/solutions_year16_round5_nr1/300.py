// run: $exec < a-small2.in > a-small2.out
#include <iostream>
#include <cstring>
#include <string>

int const maxn = 60;
int f[maxn][maxn];
bool vis[maxn][maxn];
std::string s;
int n;

int calc(char ch1, char ch2)
{
	if (ch1 == ch2) return 10;
	else return 5;
}

int dp(int l, int r)
{
	int & ret = f[l][r];
	if (vis[l][r]) return ret;
	vis[l][r] = true;
	if (l > r) return ret = 0;
	for (int i = l + 1; i <= r; i += 2)
		ret = std::max(ret, calc(s[l - 1], s[i - 1]) + dp(i + 1, r) + dp(l + 1, i - 1));
	return ret;
}

int main()
{
	std::ios::sync_with_stdio(false);
	int T; std::cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		std::cout << "Case #" << ti << ": ";
		std::cin >> s;
		n = s.size();
		std::memset(vis, 0, sizeof(vis));
		std::memset(f, 0, sizeof(f));
		std::cout << dp(1, n) << '\n';
	}
}

