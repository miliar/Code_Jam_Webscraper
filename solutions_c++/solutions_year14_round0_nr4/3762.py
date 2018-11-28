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

pii war(set<double> a, set<double> b)
{
	pii rv = mp (0,0);
	for (auto it = a.end(); it != a.begin();)
	{
		it--;
		auto qt = b.lower_bound(*it);
		if (qt == b.end())
		{
			rv.first++;
			a.erase(it);
			it = a.end();
			b.erase(b.begin());
		}
		else
		{
			rv.second++;
			a.erase(it);
			it = a.end();
			b.erase(qt);
		}
	}
	
	return rv;
}

pii deceitful_war(set<double> a, set<double> b)
{
	pii rv = mp(0, 0);
	for (auto it = a.begin(); it != a.end(); )
	{
		//it++;
		if (*it < *b.begin())
		{
			rv.second++;
			a.erase(it);
			it = a.begin();
			auto jt = b.end();
			jt--;
			b.erase(jt);
		}
		else
		{
			rv.first++;
			a.erase(it);
			it = a.begin();
			b.erase(b.begin());
		}
	}
	return rv;
}

int main()
{
	ifstream in("D-large.in");
	ofstream out("D.out");
	int t;
	in >> t;
	int n;
	REP1(II, t)
	{
		in >> n;
		set<double> a, b;
		double qq;
		REP(i, n)
		{
			in >> qq;
			a.insert(qq);
		}
		REP(i, n)
		{
			in >> qq;
			b.insert(qq);
		}
		
		pii r1 = war(a, b);
		pii r2 = deceitful_war(a, b);
		out << "Case #" << II << ": " << r2.first<< " " << r1.first << "\n";
		
	}
	
	out.close();
	in.close();
	return 0;
}