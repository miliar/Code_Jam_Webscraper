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
int A[maxN];

//init
inline void init()
{
	scanf("%d", &t);
}

//Solve
inline void solve()
{
	int a, b, c;
	for (int x = 1; x <= t; x++)
	{
		scanf("%d %d %d", &a, &b, &c);
		printf("Case #%d: ", x);
		if (b*c % a != 0) printf("RICHARD");
		else
		{
			if (a == 1 || a == 2)	printf("GABRIEL");
			else if (a == 3)
			{
				if (min(b, c) == 1) printf("RICHARD");
				else printf("GABRIEL");
			}
			else
			{
				if (min(b, c) == 1) printf("RICHARD");
				else if (min(b, c) >= 3) printf("GABRIEL");
				else printf("RICHARD");
			}
		}
		printf("\n");
	}
}


int main()
{
	//ios_base::sync_with_stdio(0); cin.tie(); cout.tie();
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	init();
	solve();
	//system("pause");
	return 0;
}