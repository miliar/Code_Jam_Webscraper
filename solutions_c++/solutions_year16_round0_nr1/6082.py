#include<iostream>
#include <fstream>
#include <set>

using namespace std;

int main()
{
	ifstream in ("A-small-attempt0.in");
	ofstream out ("output.txt");
	int n;
	in>>n;
	int number;
	for (int i = 1; i <= n; i++)
	{
		in>>number;
		int numberD = number;
		set<int> s;
		int j = 1;
		if (number == 0) out<<"Case #"<<i<<": "<<"INSOMNIA"<<'\n';
		else
		{
			while (s.size() != 10)
			{
				number = numberD * j;
				int r;
				int d = number;
				do
				{
					r = d % 10;
					d = d / 10;
					s.insert(r);
				} while(d != 0 );
				j++;
			}
			out<<"Case #"<<i<<": "<<number<<'\n';
		}
		
	}
	return 0;
}
