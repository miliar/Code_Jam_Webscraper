#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))
const double eps = 1e-10;
const int N = 710;
int a[N];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		int x;
		int n, m;
		cin >> n >> m;
		MEM(a, 0);
		int maxv = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> x;
			a[x]++;
			maxv = max(x, maxv);
		}
		int ret = 0;
		for (int i = maxv; i > 0; i--)
		{
			if (!a[i]) continue;
			if (a[i])
			{
				if (a[i] > 1 && i + i <= m) ret += a[i] / 2, a[i] &= 1;
				if (a[i] == 0) continue;
				for (int j = i - 1; j > 0; j--)
				{
					if (!a[j]) continue;
					if (j + i > m) continue;
					int tmp = min(a[i], a[j]);
					ret += tmp;
					a[i] -= tmp;
					a[j] -= tmp;
					if (a[i] == 0) break;
				}
				ret += a[i];
			}
		}
		printf("Case #%d: %d\n", ks++, ret);
	}
	return 0;
}