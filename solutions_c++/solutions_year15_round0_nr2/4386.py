#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <bitset>
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);

const int MAXN = 100001;
string s;
int a[MAXN];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	for (int t = 0; t < tt; t++)
	{
		int d;
		cin >> d;
		for (int i = 0; i < d; i++) cin >> a[i];
		int ans = 1000 * 10;
		for (int eat = 1; eat < 1001; eat++)
		{
			int mv = 0;
			for (int i = 0; i < d; i++)
			{
				mv += (a[i] - 1) / eat;
			}
			ans = min(ans, eat + mv);
		}
		cout << "Case #" << t + 1 << ": " <<  ans << endl;
	}
	return 0;
}