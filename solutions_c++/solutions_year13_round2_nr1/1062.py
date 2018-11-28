#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <list>
#include <string>
#include <sstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int m,n;
long long a[1000];

int main()
{
	int t,tt,i,j;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>m>>n;
		for(i=0; i<n; ++i)
			fin>>a[i];
		sort(a, a+n);
		long long best = 10000000000;
		int c = 0;
		for(i=0; i<n; ++i)
		{
			if(a[i] < m)
				m+=a[i];
			else
			{
				if(best > c + n - i)
					best = c+n-i;

				if(m == 1) 
				{
					c = best + 1;
					break;
				}

				while(m <= a[i])
				{
					c++;
					m+=m-1;
				}
				--i;
			}
		}
		if(best > c)
			best = c;
		fout<<"Case #"<<t<<": "<<best<<endl;
	}
	return 0;
}
