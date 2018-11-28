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
const int N = 1010;
int a[N];
int b[N];
int check(int k, int n)
{
	int ret = 0;
	memcpy(b, a, sizeof(a));
	int l, r;
	l = r = k;
	for (int i = 0; i < n; i++)
	{
		int maxv = -1;
		int t = -1;
		for (int j = 0; j < n; j++)
		{
			if (j >= l && j <= r) continue;
			if (maxv < b[i]) maxv = b[i], t = j;
		}

	}
	return ret;
}
int main()
{
	//freopen("input.txt", "r", stdin);
	
	//freopen("B-small-attempt1.in", "r", stdin);
	//freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);

	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) cin >> a[i];
		int l = 0;
		int r = n - 1;
		int ans = 0;
		while (l <= r)
		{
			int minv = 1e9 + 1;
			int k = -1;
			for (int i = l; i <= r; i++)
			{
				if (minv > a[i]) minv = a[i], k = i;
			}
			if (k - l >= r - k)
			{
				for (int i = k; i < r; i++) swap(a[i], a[i + 1]), ans++;
				r--;
			}
			else
			{
				for (int i = k; i > l; i--) swap(a[i], a[i - 1]), ans++;
				l++;
			}
		}
		printf("Case #%d: %d\n", ks++, ans);
	}
	return 0;
}