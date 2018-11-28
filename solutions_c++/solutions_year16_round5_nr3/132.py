#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000ll;
const double eps = 1e-8;

struct vec3
{
	int x, y, z;
	vec3() { x = y = z = 0;  }
	vec3(int x, int y, int z) : x(x), y(y), z(z) {}

	double length() { return sqrt(x * x + y * y + z * z); }
};

vec3 operator + (const vec3 &a, const vec3 &b) { return vec3(a.x + b.x, a.y + b.y, a.z + b.z); }
vec3 operator - (const vec3 &a, const vec3 &b) { return vec3(a.x - b.x, a.y - b.y, a.z - b.z); }

int n, s;
vec3 p[1005], v[1005];

double dp[1005];
bool used[1005];

void dij(int start)
{
	for (int i = 0; i < n; i++)
	{
		dp[i] = 1e20;
		used[i] = false;
	}

	dp[start] = 0.0;

	while (true)
	{
		int id = -1;
		double idvalue = 1e20;
		for (int i = 0; i < n; i++)
			if (!used[i] && dp[i] < 1e19 && dp[i] < idvalue)
			{
				idvalue = dp[i];
				id = i;
			}

		if (id == -1)
			break;

		used[id] = true;

		for (int i = 0; i < n; i++)
			if (id != i)
				dp[i] = min(dp[i], max(dp[id], (p[i] - p[id]).length()));
	}
}

void solve()
{
	scanf("%d%d", &n, &s);
	for (int i = 0; i < n; i++)
	{
		int x, y, z;
		scanf("%d%d%d", &x, &y, &z);
		p[i] = vec3(x, y, z);
		scanf("%d%d%d", &x, &y, &z);
		v[i] = vec3(x, y, z);
	}

	dij(0);
	printf("%.8lf", dp[1]);

	printf("\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
	{
		fprintf(stderr, "Test #%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
