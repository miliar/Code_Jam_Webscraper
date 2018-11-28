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

int a[5][5];
int b[5][5];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int tt;
	cin >> tt;
	for (int t = 0; t < tt; t++)
	{
		int i1;
		cin >> i1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> a[i][j];
				
		int i2;
		cin >> i2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> b[i][j];
		
		int cnt = 0;
		int ans = 0;
		
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (a[i1 - 1][i] == b[i2 - 1][j])
				{
					cnt++;
					ans = a[i1 - 1][i];
				}
				
		if (!cnt)
		{
			printf("Case #%d: Volunteer cheated!\n", t + 1);
		}
		else if (cnt == 1)
		{
			printf("Case #%d: %d\n", t + 1, ans);
		}
		else
		{
			printf("Case #%d: Bad magician!\n", t + 1);
		}
	}
	
	return 0;
}





