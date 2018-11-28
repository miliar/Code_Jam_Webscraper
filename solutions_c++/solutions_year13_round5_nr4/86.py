#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;



int n;
string s;
long double dp[1 << 20];

void Load()
{
	getline(cin, s);
	n = s.length();
}



long double f(int m)
{
	//cerr << "dp " << m << " " << "\n";
	if (dp[m] >= 0) return dp[m];
	if (m+1 == (1 << n)) return 0;
	int i, j;
	int l[20];
	for (j = 0; m & (1 << j); j++) {
		; 
	}
	l[j] = 0;
	for (i = 1; i < n; i++) {
		l[(j+i) % n] = l[(j+i-1) % n] + 1;
		if ((m & (1 << ((j+i) % n))) == 0)
			l[(j+i) % n] = 0;
	}
	long double ans = 0;
	for (i = 0; i < n; i++)
		ans += (f(m | (1 << ((n + i - l[i]) % n))) + n - l[i]) / n;
	dp[m] = ans;
	return ans;
}


void Solve()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int start;
	int i, j;
	start = 0;
	j = 1;
	for (i = 0; i < n; i++) {
		start <<= 1;
		if (s[i] == 'X')
			start |= 1;
	}
	for (i = 0; i < (1 << n); i++)
		dp[i] = -1;
	cout << f(start) << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	getline(cin, s);
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
