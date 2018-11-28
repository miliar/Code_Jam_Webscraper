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
long long p;

void Load()
{
	cin >> n >> p;
}


long long MinCanLoose(long long b, long long s, long long cnt, long long p)
{
	if (p == 0) return b;
	if (p >= cnt) return (1LL << n);
	long long p1 = min (p, cnt >> 1);
	long long p2 = p - p1;
	return min(MinCanLoose(b, s << 1, cnt >> 1, p1), MinCanLoose(b+s, s << 1, cnt >> 1, p2));
}

long long MaxCanWin(long long b, long long s, long long cnt, long long p)
{
	if (p == 0) return 0;
	if (p >= cnt) return b + s * (cnt-1);
	long long p1 = min (p, cnt >> 1);
	long long p2 = p - p1;
	return max(MaxCanWin(b, s << 1, cnt >> 1, p1), MaxCanWin(b+s, s << 1, cnt >> 1, p2));
}


void Solve()
{
	long long end = (1LL << n);
	cout << MinCanLoose(0, 1, end, p)-1 << ' ' << MaxCanWin(0, 1, end, p) << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
