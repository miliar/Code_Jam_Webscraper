#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <deque>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)

int main()
{
	ifstream in("B-large.in");
	ofstream out("output.txt");
	int t;
	in>>t;
	int a[105][105];
	for (int q = 1; q <= t; q++)
	{
		int m,n;
		in>>n>>m;
		out<<"Case #"<<q<<": ";
		REP(i,n)
			REP(j,m)
				in>>a[i][j];
		bool yes = true;
		REP(i,n)
			REP(j,m)
			{
				bool ud = false, lr = false;
				REP(e,n)
					if (a[e][j] > a[i][j]) ud = true;
				REP(e,m)
					if (a[i][e] > a[i][j]) lr = true;
				if (lr && ud) 
				{
					yes = false;
					break;
				}
			}
		if (yes) out<<"YES\n";
		else out<<"NO\n";

	}
	in.close();
	out.close();
	return 0;
}