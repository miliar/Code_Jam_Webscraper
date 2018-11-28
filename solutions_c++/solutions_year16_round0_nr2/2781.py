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

const ld PI = acos(-1.0);

bool w[10];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int iter = 1; iter <= n; iter++)
	{
		string s;
		cin >> s;
		s += '+';
		int ans = 0;
		for (int i = s.length() - 2; i >= 0; i--) 
			if (s[i] != s[i + 1]) ans++;
		cout << "Case #" << iter << ": " << ans << endl;
	}
	return 0;
}