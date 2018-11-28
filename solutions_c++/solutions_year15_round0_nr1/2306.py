#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <math.h>
#include <sstream>
#pragma comment (linker, "/STACK:167177216")
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for( it = coll.begin(); it != coll.end(); ++it)
const int MAXN = 9;
typedef long long LL;



int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; test++)
	{
		int n;
		cin >> n;
		string s;
		cin >> s;

		int ans = 0;
		int temp = 0;
		for (int i = 0; i <= n; i++)
		{
			if (i <= temp)
			{
				temp += (s[i] - '0');
			}
			else
			{
				ans += (i - temp);
				temp = i;
				temp += (s[i] - '0');
			}

		}
		cout << "Case #" << test << ": " << ans << endl;
	}



    return 0;
}