
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <cctype>
#include <map>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

void main()
{
	int T;
	ofstream out;
	ifstream in;
	in.open("A-large.in", ios_base::in);
	out.open("outA.out", ios_base::app);
	in>>T;
	for(int t = 0; t < T; ++t)
	{
		int ans1 = 0, ans2 = 0;
		int n;
		in>>n;
		int *m = new int [n];
		int last = 0;
		int speed = 0;
		for(int i = 0; i < n; ++i)
		{
			in>>m[i];
			if(last <= m[i])
			{
				last = m[i];
			}
			else
			{
				if(last - m[i] > speed)
					speed = last - m[i];
				ans1 += last - m[i];
				last = m[i];
			}
		}
		for(int i = 0; i < n - 1; ++i)
		{
			ans2 += min(speed, m[i]);
		}
		out<<"Case #"<<t + 1<<": "<<ans1<<' '<<ans2<<endl;
	}
	system( "pause" );
}
