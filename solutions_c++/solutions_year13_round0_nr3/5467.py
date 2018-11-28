#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

string convert( long long i ) 
{
	stringstream O;
	O<<i;
	return O.str();
}

int main()
{
	int n;
	ifstream cin("input.txt");
	ofstream fout("out.txt");

	cin>>n;
	for(int u = 0; u < n ; u++)
	{
		int count = 0;
		fout<<"Case #"<<u+1<<": ";
		long long a, b;
		cin>>a>>b;
		long long a1 = (long long)ceil(sqrt((long double)a));
		long long a2 = (long long)floor(sqrt((long double)b));

		for(long long i = a1; i <= a2; i++)
		{
			string t1 = convert(i);
			string t2 = t1;
			reverse(t1.begin(), t1.end());
			if(t1 == t2)
			{
				string T1 = convert(i*i);
				string T2 = T1;
				reverse(T1.begin(), T1.end());
				if(T1 == T2)
					count++;
			}
		}
		fout<<count<<endl;
	}
	return 0;
}