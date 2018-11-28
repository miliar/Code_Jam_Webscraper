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
const LL INF = 1e9 + 7;
const int N = 1e5 + 10;

int getans(LL n)
{
	int a[10];
	MEM(a, 0);
	int cnt = 0;
	for (int i = 1; i <= 1000; i++)
	{
		LL t = i*n;
		while (t)
		{
			if (a[t % 10] == 0) a[t % 10] = 1, cnt++;
			t /= 10;
		}
		if (cnt == 10)
		{
			return (LL)n*i;
		}
	}
	return -1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	LL n;
	int ks = 1;
	while (ncase--)
	{
		cin >> n;
		int ans = getans(n);
		if (ans == -1) printf("Case #%d: INSOMNIA\n", ks++);
		else printf("Case #%d: %d\n", ks++, ans);
	}
	return 0;
}