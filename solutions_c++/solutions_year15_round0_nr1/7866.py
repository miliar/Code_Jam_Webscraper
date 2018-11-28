#pragma warning (disable : 4996)
#pragma comment(linker, "/STACK:36777216")



#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <ios>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <queue>
#include <set>
#include <functional>
#include <cmath>
#include <sstream>
#include <map>
#include <memory.h>
#include <stdio.h>
#include <cassert>
#include <string.h>
#include <deque>
#include <ctime>

#define forn(i , n) for (int i = 0; i < n; ++i)
#define down(i, n) for (int i = n - 1; i >= 0; --i)


using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;
typedef vector<int> vint;
typedef vector<i64> vi64;
typedef pair<int, int> pint;
typedef pair<i64, i64> pi64;

#define FILE_NAME "file"
#define CONTEST "seq"
#define M_PI 3.14159265358979323846



const i64 inf = 100000000000000000LL;

#define MOD 10000000000007 




int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout << fixed << setprecision(15);
	srand(23);

#ifdef FILE_INPUT
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
//#else 
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	forn(t, T)
	{
		int n;
		cin >> n;
		string s;
		cin >> s;
		int ans = 0;
		int c = 0;
		forn(i, n + 1)
		{
			if (c < i)
			{
				ans += i - c;
				c++;
			}
			else
			{

			}
			c += s[i]-'0';
		}
		cout << "Case #" << (t + 1) << ": " << ans << "\n";
	}
	return 0;
}