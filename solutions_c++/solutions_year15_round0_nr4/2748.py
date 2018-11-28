
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <map>
#include <deque>
#include <list>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

void main()
{
	int T;
	ifstream in;
	ofstream out;
	in.open("D-small-attempt0.in", ios_base::in);
	out.open("outD.out", ios_base::app);
	in>>T;
	for(int t = 0; t < T; ++t)
	{
		int x, r, c;
		in>>x>>r>>c;
		out<<"Case #"<<t + 1<<": ";
		if(x - 1 > r || x - 1 > c || (r * c) % x)
		{
			out<<"RICHARD\n";
		}
		else
			out<<"GABRIEL\n";
	}
	in.close();
	out.close();
	system("pause");
}
