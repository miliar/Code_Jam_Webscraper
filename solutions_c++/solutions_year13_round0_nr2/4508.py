#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
#include <sstream>

using namespace std;

void find_min(const int& n, const int& m, const vector<vector<int> >& v, const vector<bool>& l, const vector<bool>& c, int& min, int& i_min, int& j_min)
{
	for(int i = 0; i < n; ++i)
	{
		if(l[i])
		{
			for(int j = 0; j < m; ++j)
			{
				if(c[j])
				{
					if(v[i][j] < min)
					{
						min = v[i][j];
						i_min = i;
						j_min = j;
					}
				}
			}
		}
	}
}

bool check_line(const int& m, const int& i, const int& value, const vector<vector<int> >& v, const vector<bool>& l, const vector<bool>& c)
{
	if(l[i])
	{
		for(int j = 0; j < m; ++j)
		{
			if(c[j] && v[i][j] != value)
				return false;
		}

		return true;
	}
	else
		return false;
}

bool check_column(const int& n, const int& j, const int& value, const vector<vector<int> >& v, const vector<bool>& l, const vector<bool>& c)
{
	if(c[j])
	{
		for(int i = 0; i < n; ++i)
		{
			if(l[i] && v[i][j] != value)
				return false;
		}

		return true;
	}
	else
		return false;
}

bool run_test(ifstream& is)
{
	int n; is >> n;
	int m; is >> m;

	vector<vector<int> > v(n);
	vector<bool> l(n, true); int l_act = n;
	vector<bool> c(m, true); int c_act = m;

	for(int i = 0; i < n; ++i)
	{
		v[i] = vector<int>(m);
		for(int j = 0; j < m; ++j)
			is >> v[i][j];
	}

	while(l_act > 0 && c_act > 0)
	{
		int min = 100;
		int i_min = 0;
		int j_min = 0;

		find_min(n, m, v, l, c, min, i_min, j_min);

		if(check_line(m, i_min, min, v, l, c))
		{
			--l_act;
			l[i_min] = false;
		}
		else if(check_column(n, j_min, min, v, l, c))
		{
			--c_act;
			c[j_min] = false;
		}
		else
			return false;
	}

	return true;
}

int main (int argc, char * const argv[])
{
	ifstream is("/Users/nathaniel/Dev/test.txt");
	int tests;
	is >> tests;

	for(int test = 0; test < tests; ++test)
	{
		cout << "Case #" << (test + 1) << ": ";

		if(run_test(is))
			cout << "YES";
		else
			cout << "NO";

		cout << endl;
	}

	return 0;
}
