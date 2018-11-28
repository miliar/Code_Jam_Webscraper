#define _CRT_SECURE_NO_WARNINGS
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstdio>
#include <complex>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
using namespace std;

const int N = 2000;
int a[N];

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif 
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n; cin >> n;
		for (int i = 0; i < n; i++) cin >> a[i];
		int ans = 1e9;
		for (int m = 1; m <= N; m++)
		{
			int res = m;
			for (int i = 0; i < n; i++)
			{
				res += (a[i] + m - 1) / m - 1;
			}
			ans = min(ans, res);
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
}