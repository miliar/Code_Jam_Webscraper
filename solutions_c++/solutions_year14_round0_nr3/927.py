#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

double val;

bool doit(vector <vector<char> > & v, int a, int b, int c)
{	 
	//cout << "test " << a << " "<< b << " " << c << endl;
	if (b >= c  && a != v.size())
	{
		//cout << "1" << endl;
	    for (size_t i = 0; i < c; ++i)
	    	v[a][i] = '.';
	    for (size_t i = 0; i < a; ++i)
		  for (size_t j = 0; j < b; ++j)
	  		v[i][j] = '.';
	    return true;
	}
	if (a >= c  && b != v[0].size())
	{
		//cout << "2" << endl;
	    for (size_t i = 0; i < c; ++i)
	    	v[i][b] = '.';
	    for (size_t i = 0; i < a; ++i)
		  for (size_t j = 0; j < b; ++j)
		  	v[i][j] = '.';

	   return true;
	}
	if (c >= 4 && a < v.size() && b < v[0].size())
	{
		for (size_t i = 0; i < a; ++i)
		  for (size_t j = 0; j < b; ++j)
	  		v[i][j] = '.';
		for (size_t i = 0; i < 2; ++i)
			v[i][b] = '.';
		for (size_t i = 0; i < 2; ++i)
			v[a][i] = '.';
		c -= 4;
		int k = 2;
		while (c > 0)
		{
			if (k < a)
			{
				v[k][b] = '.';
			    --c;
			}
			if (c > 0 && k < b)
			{
				v[a][k] = '.';
			    --c;
			}
			++k;
	    }
		return true;
	}
	return false;

}

int doit(vector <vector<char> > & v, int d)
{
	//cout << "start " <<  d << " " << v.size() << " " << v[0].size() << endl;
	if (v.size() == 1 || v[0].size() == 1 || d == v.size() * v[0].size())
	{
		for (size_t i = 0; i < v.size(); ++i)
			for(size_t j = 0; j < v[0].size(); ++j)
			{
				v[i][j] = '.';
				--d;
				if (!d)
				{
					v[0][0] = 'c';
						return 0; 
				}
			}
	}
	if (d == 1)
	{
		v[0][0] = 'c';
		return 0;
	}
	for (size_t i = 2; i <= d; ++i)
	{
		for (size_t j = i; j <= d; ++j)
		{
			int a = i;
			int b = j;
			if (a * b > d)
				continue;
			int c = d % (a * b);
			if (a * b > d)
				continue;
			if (a * b + c != d)
				continue;
			if (a + b - 1 <= c)
				continue;
			if (c == 1)
				continue;
			if (a <= v.size() && b <= v[0].size() && doit(v, a, b,c))
				return 0;
			swap(a, b);
			if (a <= v.size() && b <= v[0].size() && doit(v, a, b, c))
				return 0;
	    }

	}
	return 1;
}

int main()
{
	fstream file("C-large.in");
	fstream output("output.txt");
	std::string s;
	std::getline(file, s);
	int n = atoi(s.c_str());
	for (int i = 0; i < n; ++i)
	{
		int r,c,m;
		file >> r >> c >> m;
		vector<std::vector<char> > v(r, vector<char>(c, '*'));
		output << "Case #" << i+1 << ": " <<  endl; //r << " " << c << " " << m << " " << endl;
		int k = doit(v, r*c - m);
		if (k == 1)
			output << "Impossible" << endl;
		else
		{
			v[0][0] = 'c';
			for (size_t i = 0; i < v.size(); ++i)
			{
				for (size_t j = 0; j < v[0].size(); ++j)
					output << v[i][j];
				output << endl;
			}
		}

	}
	file.close();
	output.close();
	return 0;
}