// run: $exec < c-small.in > c-small.out
#include <iostream>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <vector>

struct data
{
	double x, y, z;
	double vx, vy, vz;
};

int const maxn = 2000;
bool vis[maxn];
bool map[maxn][maxn];
std::vector<data> da;
int n, s;

double dis(data const& a, data const& b)
{
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) + (a.z - b.z) * (a.z - b.z));
}

bool dfs(int x)
{
	if (!x) return true;
	vis[x] = true;
	for (int i = 0; i < n; i++)
		if (!vis[i] && map[i][x]) if (dfs(i)) return true;
	return false;
}

bool judge(double len)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (dis(da[i], da[j]) <= len) map[i][j] = true;
			else map[i][j] = false;
	memset(vis, 0, sizeof(vis));
	if (dfs(1)) return true;
	return false;
}

int main()
{
	int T; std::cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		std::cout << "Case #" << ti << ": ";
		std::cin >> n >> s;
		da.clear(); da.resize(n);
		for (int i = 0; i < n; i++) std::cin >> da[i].x >> da[i].y >> da[i].z >> da[i].vx >> da[i].vy >> da[i].vz;
		double l = 0, r = 5000;
		for (int i = 0; i < 200; i++) {
			double mid = (l + r) / 2.0;
			if (judge(mid)) r = mid;
			else l = mid;
		}
		std::cout << std::fixed << std::setprecision(7) << l << '\n';
	}
}

