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
		int X, R, C;
		cin >> X >> R >> C;
		string ans;
		if (X == 1) ans = "GABRIEL";
		else ans = "RICHARD";
		if (X == 2)
		{
			if (R*C % X != 0) ans = "RICHARD";
			else ans = "GABRIEL";
		}
		if (X == 3)
		{
			if (R*C % X == 0 && R*C != 3) ans = "GABRIEL";
			else ans = "RICHARD";
		}
		if (X == 4)
		{
			if (R*C % X == 0 && (R*C == 12 || R*C == 16)) ans = "GABRIEL";
			else ans = "RICHARD";
		}


		cout << "Case #" << test << ": " << ans << endl;
	}



    return 0;
}