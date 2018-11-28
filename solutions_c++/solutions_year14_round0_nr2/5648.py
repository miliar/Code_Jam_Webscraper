/*
	Author: Zhaohai Nathaniel Lee <Nathanielben@gmail.com> @ inspiratune.com
*/

// Include the header files
#include <iostream>
#include <iterator>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstdio>

#define IN "B-large.in"
#define OUT "B-larges.out"

//Set the namespace
using namespace std;

typedef pair < double, double >pdd;

ostream& operator<<(ostream& out, const pdd& p) {
  return out << p.first << "\t" << p.second;
}

int cmp(const pdd& x, const pdd& y)
{
	return x.second < y.second;
}

double tt_time(int turn, double increase, double st_cost, double *vi);

int main(int argc, char const *argv[])
{
	ifstream cin(IN);
	ofstream cout(OUT);
	freopen(IN, "r", stdin);
	freopen(OUT, "w", stdout);

	int r = 0;
	cin >> r;

	for (int i = 0; i < r; ++i)
	{
		int n = 0;
		double t = 0.0, c = 0.0, f = 0.0, x = 0.0, v0 = 2.0;
		double t_all, t_none;
		double* v = &v0;

		cin >> c >> f >> x;
		n = (int)(x / c);

		map<double, double> mp1;
		vector<pdd> vec;
		map<double ,double >::iterator it;

		t_none = x / 2.0;
		mp1.insert(pdd(0,t_none));

		for (int j = 0; j < n; ++j)
		{
			*v = 2.0;

			mp1.insert(pdd(j,(tt_time(j, f, c, v)+x / *v)));
		}

		*v = 2.0;
		t_all = tt_time(n, f, c, v) + x / *v;
		mp1.insert(pdd(n,t_all));

		for (map<double,double>::iterator curr = mp1.begin(); curr != mp1.end(); ++curr)
		{
			vec.push_back(make_pair(curr->first, curr->second));
		}
		sort(vec.begin(), vec.end(), cmp);
		t = vec.front().second;
		printf("Case #%d: %lf\n", i+1, t);

		mp1.clear();
	}
	fclose(stdin);
	fclose(stdout);
	cin.close();
	cout.close();
	return 0;
}

double tt_time(int turn, double increase, double st_cost, double *vi)
{
	double r_time = 0.0;
	for (int i = 0; i < turn; ++i)
	{
		r_time += st_cost / *vi;
		*vi += increase;
	}
	return r_time;
}