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
#include <stack>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define REP1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define wait system("pause")

int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("A.out");
	int t;
	int a[4][4];
	int b[4][4];
	int q, w;
	in >> t;
	REP1(II, t)
	{
		set<int> vv;
		in >> q;
		q--;
		REP(i, 4)
			REP(j, 4)
			in >> a[i][j];
		in >> w;
		w--;
		REP(i, 4)
			REP(j, 4)
			in >> b[i][j];

		
		REP(i,4)
			REP(j,4)
				if (a[q][i] == b[w][j])
					vv.insert(a[q][i]);
		
		out << "Case #" << II << ": ";
		if (vv.size() == 1)
			out << *vv.begin();
		else if (vv.size() == 0)
		{
			out << "Volunteer cheated!";
		}
		if (vv.size() > 1)
		{
			out << "Bad magician!";
		}
		out << "\n";
	}
	out.close();
	in.close();
	return 0;
}