#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <bitset>
#define y1 y11
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);

bool w[10];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		memset(w, 0, sizeof(w));
		int cn = 0;
		int v;
		cin >> v;
		int ans = -1;
		for (int iter = 1; iter <= 1003; iter++)
		{
			int dv = v * iter;
			while (dv > 0)
			{
				int d = dv % 10;
				if (!w[d]) w[d] = true, cn++;
				dv /= 10;
			}
			if (cn == 10) 
			{
				ans = v * iter;
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (ans == -1) cout << "INSOMNIA" << endl;
		else cout << ans << endl;
	}
	return 0;
}