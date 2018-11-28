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
#include <numeric>
#include <iomanip>
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
	ifstream in("B-large.in");
	ofstream out("B.out");
	int t;
	in >> t;
	double x, c, f;
	
	REP1(II, t)
	{
		in >> c >> f >> x;
		double temp = 0;
		double hh = 0;
		double gg = 0;
		double aa = 0;
		double tt = 0;
		double z = 2;
		int k = 0;
		while (1)
		{
			tt = c / z;
			gg = x / z;
			if (gg <= tt)
			{
				temp += gg;
				break;
			}
			else if (gg <= (tt + x / (z + f)))
			{
				temp += gg;
				break;
			}
			else
			{
				temp += tt;
				z += f;
			}
		}
		out << "Case #" << II << ": ";
		out << fixed << setprecision(10) << temp;
		out << "\n";
	}
	out.close();
	in.close();
	return 0;
}