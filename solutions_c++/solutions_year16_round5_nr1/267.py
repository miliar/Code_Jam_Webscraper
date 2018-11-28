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
#define rnd() ((rand() << 15) + rand())
#define y1 y11
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
const ld PI = acos(-1);



string s;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cout << "Case #" << test << ": ";
		int c = 0;
		int j = 0;
		cin >> s;
		int ans = 0;
		int cn = 0, lst = -1;
		for (int i = 0; i < s.length(); i++)
		{
			int vl = 0;
			if (s[i] == 'J') vl = 1;
			if (lst == vl)
			{
				cn--;
				ans++;
				lst = ((cn==0)?-1:(1-lst));
			}
			else cn++, lst = vl;
		}
		cout << ans * 10 + 5 * (s.length() / 2 - ans) << endl;
	}
	return 0;
}