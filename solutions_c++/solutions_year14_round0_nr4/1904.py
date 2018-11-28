#include <iostream>
#include <stdio.h>
#include <list>
#include <algorithm>

using namespace std;

int T;
int N;

#define MAX 1004
list<double> a, b;
int war, dwar;

bool sortfn(double x, double y) { return(x < y);}

int main()
{
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			double val;
			cin >> val;
			a.push_back(val);
		}
		for (int j = 0; j < N; j++)
		{
			double val;
			cin >> val;
			b.push_back(val);
		}

		a.sort();
		b.sort();
		
		list<double> c = b;
		reverse(c.begin(), c.end());

		int m, n;

		list<double> d = a;
		reverse(d.begin(), d.end());

		m = 0;
		for (int j = 0; j < N; j++)
		{
			list<double>::iterator it = a.begin();
			list<double>::iterator k;
			int flag = 0;
			for (k = b.begin(); k != b.end(); k++)
				if (*it < *k)
				{
					k = b.erase(k);
					flag = 1;

					break;
				}
			if (flag == 0)
				m++;
			a.pop_front();
		}

		n = 0;
		for (int j = 0; j < N; j++)
		{
			list<double>::iterator it = d.begin();
			list<double>::iterator k = c.begin();

			if (*it < *k)
			{
				d.pop_back();
			}
			else
			{
				d.pop_front();
				n++;
			}
			c.pop_front();
		}

		a.clear();
		b.clear();
		c.clear();
		d.clear();

		cout << "Case #" << i << ": " << n << " " << m << endl;
	}
	return 0;
}
