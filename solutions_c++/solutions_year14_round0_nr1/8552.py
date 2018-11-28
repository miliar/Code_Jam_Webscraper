#include"stdafx.h"
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<queue>
#include<math.h>
#include<vector>
#include<deque>
#include<stack>
#include<set>
#include<sstream>
#include<algorithm>

using namespace std;


#pragma warning(disable : 4996)
#define mp(a,b) (make_pair(a,b))
#define mms memset
#define LL long long
#define y1 y1111
#define eps 1e-9
#define y2 y2222
#define LINF LLONG_MAX
#define INF 1000000000
#define PI 3.14159265359
#define mod 1000000007
#define x1 x1111
#define x2 x2222
#define pow10 pppp

int main(void)
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	int arr[4][4];
	int r;
	set<int> s;
	int ans = 0,f;
	for (int a = 0; a < t; a++)
	{
		ans = 0;
		f = 0;
		s.clear();
		cin >> r;
		r--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> arr[i][j];
			}
		}
		for (int i = 0; i < 4; i++)
		{
			s.insert(arr[r][i]);
		}
		cin >> r;
		r--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> arr[i][j];
				if (i == r)
				{
					if (s.find(arr[i][j]) != s.end())
					{
						ans++;
						f = arr[i][j];
					}
				}
			}
		}
		if (ans == 1)
		{
			cout << "Case #" << a + 1 << ": " << f << '\n';
		}
		else if (ans == 0)
		{
			cout << "Case #" << a + 1 << ": Volunteer cheated!\n";
		}
		else
		{
			cout << "Case #" << a + 1 << ": Bad magician!\n";
		}
	}
	
}
