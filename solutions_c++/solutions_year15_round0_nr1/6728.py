#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <fstream>
#include <stack>
#include <limits.h>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define SZ(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
using namespace std;
double PI = 3.1415926536;
int dX[] = { 1, -1, 0, 0 };
int dY[] = { 0, 0, 1, -1 };
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	FOR(T, 1, t + 1)
	{
		long long int x, res = 0, sum = 0;
		string s;
		cin >> x >> s;
		FOR(i, 0, SZ(s))
		{
			sum += s[i] - '0';
			if (sum < i + 1)
				res += i + 1 - sum, sum += i + 1 - sum;
		}
		cout << "Case #" << T << ": " << res << "\n";
	}
}