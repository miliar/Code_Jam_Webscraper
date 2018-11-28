#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <ctype.h>
#include <cassert>
#include <stack>

using namespace std;


#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left

template < typename T > T abs(T x)
{
	return x > 0 ? x : -x;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int tt;
	cin >> tt;
	for (int t = 0; t < tt; t++)
	{
		ld c, f, x;
		cin >> c >> f >> x;
		
		ld ans = 1e18;
		
		ld curr = 0.0;
		
		for (int i = 0; i < 1000000; i++)
		{
			ans = min(ans, curr + x / (2.0 + f * i));
			curr += c / (2.0 + f * i);
			
			if (curr > 2.0 * ans)
				break;
		}
				
		cout.precision(7);
		
		cout << "Case #" << t + 1 << ": ";
		cout << fixed << ans << endl;
	}
	
	return 0;
}






