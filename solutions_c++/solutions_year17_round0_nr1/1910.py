#define _CRT_SECURE_NO_WARNINGS
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <iterator>
#include <ostream>
#include <iomanip>
#include <cstring>
#include <sstream>
#include <cassert>
#include <cstdlib>
#include <istream>
#include <fstream>
#include <climits>
#include <complex>
#include <memory>
#include <string>
#include <bitset>
#include <vector>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef complex <ld> cd;

const bool db = false;

#define fs first
#define X first 
#define ft first

#define sd second
#define Y second
#define sc second

#define mp make_pair
#define pb push_back
#define ppb pop_back

#define inf 1000000007
#define nmax 100100
#define mmax 100100
#define eps 1e-12
const int mod7 = 1e9 + 7;

string solve(string s, int k)
{
	int n = s.length();
	int inv = 0;
	for(int i = 0; i < n-k+1; i++)
	{
		if(s[i] == '-')
		{
			inv++;
			for(int j = 0; j < k; j++)
			{
				s[i + j] = ((s[i + j] == '-') ? '+' : '-');
			}
		}
	}
	bool flag = true;
	for(int i = 0; i < n; i++)
	{
		if (s[i] != '+')
			flag = false;
	}
	if (flag)
		return to_string(inv);
	return "IMPOSSIBLE";
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++){
		int k;
		string s;
		cin >> s >> k;
		cout << "Case #" << i << ": " << solve(s, k) << "\n";
	}
}