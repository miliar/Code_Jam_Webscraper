#include <ctime>
#include <bitset>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <fstream>
using namespace std;


#define PB	push_back
#define MP  make_pair
#define ALL(a) 	(a).begin(), (a).end()
#define FILL(a,v) memset(a,v,sizeof(a))

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define SQR(x) (x)*(x)

typedef long long ll;

const double PI = acos(-1.0);
const double EPS = 1e-7;
const int MOD = 1000000007;
const int INF = 2000000000;


bool u[10010];
int a[10010];
int s;
int n;
void solve()
{
	scanf("%d", &n);
	scanf("%d", &s);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);
		a[i]=-a[i];
		u[i] = false;
	}

	sort(a, a+n);
	for (int i=0;i<n;++i)a[i]=-a[i];
	int p = n;
	int res = 0;
	while(p)
	{
		int pos=0, rest;
		for (int i = 0; i < n; ++i)
		{
			if (u[i] == false)
			{
				--p;
				pos = i;
				rest = s-a[i];
				u[i] = true;
				break;
			}
		}

		for (int i = 0; i < n; ++i)
		{
			if (u[i] == false && a[i] <= rest)
			{
				u[i] = true;
				--p;
				break;
			}
		}
		++res;
	}
	cout << res;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	clock_t st = clock();
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; ++test)
	{
		clock_t stt = clock();
		printf("Case #%d: ", test);
		solve();
		printf("\n");
		cerr << test << ": " << (clock()-stt+0.0)/CLOCKS_PER_SEC << endl;
	}

	cerr << "----\n" << (clock()-st+0.0)/CLOCKS_PER_SEC;
	return 0;
} 
