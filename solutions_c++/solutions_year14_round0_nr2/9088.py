// CodeJamQualification.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <utility>
#include <memory>
#include <malloc.h>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <time.h>
#include <algorithm>
#include <queue>
#include <complex>
#include <hash_map>
#include <hash_set>
#include <functional>
#include <list>
#include <stack>
#include <assert.h>
#include <iterator>
#include <numeric>
#include <deque>
#include <bitset>
#include <limits>
#include <sstream>

using namespace std;

// #define rall(v) v.begin(), v.end()
#define all(v) v.begin(), v.end()
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)

typedef long long i64;
typedef unsigned long long u64;
typedef pair<int, int> pii;
typedef pair<int, int> pll;
typedef complex<double> cplx;

#pragma comment(linker, "/STACK:167772160")

const int INF		= 1e9;
const double EPS	= 1e-9;
const double pi		= acos(-1.);
const double PI		= 3.1415926535897932384626433832795028841971693993751058;


void prB()
{
	ifstream fcin("D:/Download/GCJ/B-small-attempt0.in");
	ofstream fcout("D:/Download/GCJ/ResB.txt");

	int n;
	fcin>>n;

	cout.precision(7);
	fcout.precision(7);

	double R = 2.0;

	vector<double> ans(n);
	for (int i = 0; i < n; ++i)
	{
		double C, F, X, t0, t1;

		fcin>>C>>F>>X;

		double k	= 1.0;
		double v0	= R;
		double v1	= R + k*F;

		t0 = X / v0;
		t1 = X / v1 + C/v0;

		double best = t0;
		while (t1 < t0)
		{
			best = t1;

			v0 = v1;
			v1 += F;

			k += 1.0;
			t0 = t1;
			t1 = t0 + C / v0 - X / v0 + X / v1;
		}

		ans[i] = best;
	}

	for (int i = 0; i < n; ++i)
	{
		cout<<"Case #"<<(i+1)<<": "<<fixed<<ans[i]<<endl;
		fcout<<"Case #"<<(i+1)<<": "<<fixed<<ans[i]<<endl;
	}
}

void prA()
{
	ifstream fcin("D:/Downloads/Contests/gcj/A-small-attempt1.in");
	ofstream fcout("D:/Downloads/Contests/gcj/ResA.txt");

	int n;
	fcin>>n;

	vector<string> ans(n);
	for (int i = 0; i < n; ++i)
	{
		int f, s;
		fcin>>f;

		vector<int> row1(4), row2(4);
		for (int j = 1; j <= 4; j++)
		{
			int a, b, c, d;
			fcin>>a>>b>>c>>d;
			if (j == f)
			{
				row1[0] = a;
				row1[1] = b;
				row1[2] = c;
				row1[3] = d;
			}
		}

		fcin>>s;
		for (int j = 1; j <= 4; j++)
		{
			int a, b, c, d;
			fcin>>a>>b>>c>>d;
			if (j == s)
			{
				row2[0] = a;
				row2[1] = b;
				row2[2] = c;
				row2[3] = d;
			}
		}

		int count = 0, res;
		for (int k = 0; k < 4; k++)
		{
			for (int l = 0; l < 4; l++)
			{
				if (row1[k] == row2[l])
				{
					count++;
					res = row1[k];
				}
			}
		}

		if (count == 1)
		{
			ans[i] = to_string((i64)res);
		}
		else if (count > 1)
		{
			ans[i] = "Bad magician!";
		}
		else
		{
			ans[i] = "Volunteer cheated!";
		}
	}

	for (int i = 0; i < n; ++i)
	{
		cout<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;
//		fcout<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;
	}
}

int main(int argc, char* argv[])
{
	prB();

	return 0;
}

