#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int a[10];
int t, n, x;
int main ()
{
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	cin >> t;
	for(int test = 1; test <= t; ++test)
	{
		cin >> n;
		if (n==0)
		{
			cout<<"Case #"<<test<<": INSOMNIA\n";
			continue;
		}
		for(int i=0;i<10;++i)
			a[i] = 0;
		int s = 10;
		x = 0;
		while(s)
		{
			x += n;
			int dx = x;
			while(dx)
			{
				int c = dx%10;
				if (!a[c])
				{
					s--;
					a[c] = 1;
				}
				dx/=10;
			}
		}
		cout<<"Case #"<<test<<": "<<x<<"\n";
	}
} 