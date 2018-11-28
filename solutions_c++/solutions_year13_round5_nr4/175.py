#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define ll long long

string s;

int n;

long double d[1 << 21];

long double get(int mask) {
	if (mask+1 == (1 << n))
		return 0.0;
	if (d[mask] > -0.5)
		return d[mask];
	d[mask] = 0.0;
	forn(i, n) {
		long double cost = n;
		int j = i;
		while(1) {
			if ((mask & (1 << j)) == 0) {
				d[mask] += cost + get(mask | (1 << j));
				break;
			}
			j = (j+1) % n;
			--cost;
		}
	}
	d[mask] /= n;
	return d[mask];
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	
	forn(tt, t) {
		cin >> s;
		int mask = 0;

		n = (int)s.length();
		forn(i, 1 << n)
			d[i] = -1;
		forn(i,s.length())
			mask |= (s[i] == 'X') * (1 << i);

		long double best = get(mask);

		printf("Case #%d: %.12llf\n", tt+1, best);
	}
	
	return 0;
}