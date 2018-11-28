#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size())
#define _USE_MATH_DEFINES
#define ll long long 
#define ull unsigned long long  
#define fname ""
const int N = (int)1e6 + 123;
const double eps = 1e-6;
const ll inf = (ll)1e18 + 123;

using namespace std;
int t, a, b;
int u[20];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for (int test = 1;test <= t;test ++)
	{
		memset(u, 0, sizeof u);
	    for (int k = 1;k < 3;k ++)
	    {
			cin >> a;
			for (int i = 1;i < 5;i ++)
				for (int j = 1;j < 5;j ++)
				{
					cin >> b;
					if (i == a)
						u[b] ++;
				}
		}
		int ans = -1, cnt = 0;
		for (int i = 1;i < 17;i ++)
			if (u[i] == 2)
			{
				ans = i;
				cnt ++;
			}
		cout << "Case #" << test << ": ";
		if (cnt == 0)
			cout << "Volunteer cheated!\n";
		else if (cnt > 1)
			cout << "Bad magician!\n";
		else
			cout << ans << endl;
	}
	return 0;
}
