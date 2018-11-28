#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stack>
#include <string.h>
#include <climits>
#include <limits>
using namespace std;

typedef vector<int> vi;

#define FOR(i, a, b) for(int i=a; i<b; i++)
#define FORE(i, a, b) for(int i=a; i<=b; i++)
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define ceil(a, b) ((a)/(b) + ((a)%(b)!=0))
#define square(a) ((a)*(a))
#define PI 3.14159265359
#define mod 1000000009LL

#define maxN 100009

int A[50000];

int main()
{

#ifdef jani
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
#endif

	int T;
	cin >> T;
	FOR(awt, 0, T)
	{
		int n, cap;
		cin >> n >> cap;
		FOR(i, 0, n) cin >> A[i];

		sort(A, A + n);

		int r = 0;

		int beg = 0;
		int end = n - 1;
		while (beg <= end)
		{
			if (A[beg] + A[end] <= cap)
			{
				beg++;
				end--;
				r++;
			}
			else
			{
				end--;
				r++;
			}
		}

		printf("Case #%d: %d\n", awt + 1, r);




	}


	return 0;
}