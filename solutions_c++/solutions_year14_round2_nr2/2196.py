#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <climits>
#include <cstdio>
#include <algorithm>
#include <list>

using namespace std;

typedef unsigned long long ull;

int main(int argc, char* argv[])
{
	if(argc < 3)
	{
		cout << "No input/output file passed as argument\n";
	}
	
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);
	
	ull t, k, a, b;
	cin >> t;
	for (ull ti = 1; ti <= t; ti++)
	{
		cin >> a >> b >> k;
		ull sum = 0;
		for(ull i = 0; i < a; i++)
		{
			for(ull j = 0; j < b; j++)
			{
				if((i & j) < k)
					sum++;
			}
		}
		cout << "Case #" << ti << ": ";
		cout << sum << "\n";
	}
	
	return 0;
}