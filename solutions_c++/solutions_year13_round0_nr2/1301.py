#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
using namespace std;
#define sz size()
#define pb push_back
#define FOR(i,a,b) for(int i = a; i < b; ++i)

int a[150][150];
int b[150];
int c[150];
int n,m;

bool check()
{
	FOR(i,0,n)
	{
		b[i] = a[i][0];
		FOR(j,1,m) b[i] = max (b[i], a[i][j]);
	}
	FOR(j,0,m)
	{
		c[j] = a[0][j];
		FOR(i,1,n) c[j] = max (c[j], a[i][j]);
	}
	
	FOR(i,0,n)
		FOR(j,0,m)
			if (a[i][j] < b[i] && a[i][j] < c[j]) return 0;
	return 1;
}

int main()
{
	freopen ("in1.txt", "r", stdin);
	freopen ("out1.txt", "w", stdout);
	
	int ppp;
	cin >> ppp;
	FOR(o,0,ppp)
	{
		cout << "Case #" << o + 1 << ": ";
	
		cin >> n >> m;
		FOR(i,0,n)
			FOR(j,0,m)
				cin >> a[i][j];
		if (check()) cout << "YES";
		else cout << "NO";
	
		cout << endl;
	}	
	return 0;
}
