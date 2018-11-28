//c++11
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cassert>
#include<stack>
#include<cstring>
#include<vector>
#include<string>
#include<cmath>
#include<ctime>
#include<set>
#include<map>
#include<queue>
#include<fstream>
#include<sstream>
#include<iomanip>
#include<complex>
#include<unordered_map>
#include<unordered_set>

#define mp(makepairtmp1,makepairtmp2) make_pair(makepairtmp1,makepairtmp2)

using namespace std;


//def
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
const int MOD = 1e9 + 9;
const double eps = 1e-5;
const int maxN = 1e3 + 10;
const int inf = 1e9;
int t, n;
char c[maxN];

//init
inline void init()
{
	scanf("%d", &t);
}

//Solve
inline void solve()
{

	for (int x = 1; x <= t; x++)
	{
		scanf("%d", &n);
		scanf("%s", c);
		int h = 0, ans = 0;
		for (int i = 0; i <= n; i++)
		{
			if (h < i)
			{
				ans += i - h;
				h = i;
			}
			h += c[i] - '0';
		}
		printf("Case #%d: %d\n", x, ans);
	}
}


int main()
{
	//ios_base::sync_with_stdio(0); cin.tie(); cout.tie();
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	init();
	solve();
	//system("pause");
	return 0;
}