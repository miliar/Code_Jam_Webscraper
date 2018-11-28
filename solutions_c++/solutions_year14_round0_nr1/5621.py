#include <ctime>
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
using namespace std;


#define PB	push_back
#define MP  make_pair
#define ALL(a) 		(a).begin(), (a).end()
#define FILL(a,v) memset(a,v,sizeof(a))

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define SQR(x) (x)*(x)

const double PI = acos(-1.0);
const double EPS = 1e-7;

const int MOD = 1000000007;

typedef long long ll;

int k;
int a[20];

void solve()
{
	FILL(a,0);
	cin >> k;
	for (int i = 1; i < 5; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			int n;
			cin >> n;
			if (i == k)
				a[n]++;
		}
	}
	cin >> k;
	for (int i = 1; i < 5; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			int n;
			cin >> n;
			if (i == k)
				a[n]++;
		}
	}
	int kk = 0;
	int nn = 0;
	for (int i = 1; i <= 16; ++i)
	{
		if (a[i] > 1)
		{
			++kk;
			nn=i;
		}
	}
	if (kk == 1)
		cout << nn;
	else if (kk > 1)
		cout << "Bad magician!";
	else if (kk < 1)
		cout << "Volunteer cheated!";
}


int main()
{
	ios_base::sync_with_stdio(false);
	freopen( "input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cout << "Case #" << test << ": ";
		solve();
		cout << endl;
	}

	return 0;
} 
