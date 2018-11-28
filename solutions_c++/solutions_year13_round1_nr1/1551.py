#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <stack>
#include <list>
#include <deque>
#include <map>
#include <bitset>
#include <string>
#include <sstream>
#include <algorithm>


using namespace std;

int main()
{
	int n;
	ifstream in("input.in");
	ofstream out("output.out");
	double pi = 3.1415926535897932384626433;
	in >> n;
	for(int cases = 1; cases <= n; cases++)
	{
		long long r, t;
		in >> r >> t;
		long long y=0;
		while(true)
		{
			if ((((r+1)*(r+1)) - (r*r)) <= t)
			{
				t -= (((r+1)*(r+1)) - (r*r));
				r+=2;
				y++;
			}
			else
				break;
		}
		out << "Case #" << cases << ": " << y << endl;
	}
	system("pause");
	return 0;
}