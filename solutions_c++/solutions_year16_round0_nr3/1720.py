#include <string>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

unsigned long long extract(int nr, int b)
{
	unsigned long long res = 0;
	while(nr > 0)
	{
		res = res * b + (nr & 1);
		nr >>= 1;
	}
	return res;
}

unsigned long long getSmallestDiv(unsigned long long tmp)
{
	if(tmp % 2 == 0)
	{
		return 2;
	}
	for(unsigned long long d = 3; d * d <= tmp; d += 2)
	{
		if(tmp % d == 0)
		{
			return d;
		}
	}
	return 1;
}

string toString(int nr)
{
	string s;
	while(nr > 0)
	{
		s.push_back('0' + (nr & 1));
		nr >>= 1;
	}
	return s;
}

void solve(ofstream& g, int n = 16, int j = 50)
{
	for(int i = 0, len = n - 2; i < (1 << len); i++)
	{
		int nr = ((1 << (n - 1)) | (i << 1) | 1);
		vector<unsigned long long> v;
		for(int b = 2; b <= 10; b++)
		{
			unsigned long long tmp = extract(nr, b);
			unsigned long long div = getSmallestDiv(tmp);
			if(div == 1)
			{
				break;
			}
			else
			{
				v.push_back(div);
			}
		}
		if(v.size() == 9)
		{
			g << toString(nr);
			for(int k = 0; k < v.size(); k++)
			{
				g << " " << v[k];
			}
			g << endl;
			j--;
		}
		if(j == 0)
		{
			break;
		}
	}
}

int main()
{
	int t;
	ifstream f("input.txt");
	ofstream g("output.txt");
	f >> t;
	int n, j;
	for(int i = 1; i <= t; i++)
	{
		f >> n >> j;
		g << "Case #" << i << ":" << endl;
		solve(g, n, j);
	}
	f.close();
	g.close();
	return 0;
}