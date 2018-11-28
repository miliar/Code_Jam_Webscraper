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


int n, x;
vector <int> a;

void Load()
{
	cin >> n >> x;
	a.resize(n);
	for (int i = 0; i < n; i++)
		cin >> a[i];
	sort(a.begin(), a.end());
}

void Solve()
{
	int i, j;
	int ans = n;
	i = 0; j = n-1;
	while ( i < j ) {
		if (a[i] + a[j] > x) j--;
		else {
			ans--;
			i++; j--;
		}
	}
	cout << ans << "\n";
}

int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
