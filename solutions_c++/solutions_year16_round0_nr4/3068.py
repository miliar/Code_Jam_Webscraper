#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int t;
long long k, c, s;
int main ()
{
	ifstream cin("D-small-attempt1.in");
	ofstream cout("output.txt");
	cin >> t;
	for(int test = 1; test <= t; ++test)
	{
		cin >> k >> c >> s;
		long long kk = 1;
		for(int j=1;j<c;++j)
			kk = kk * k;
		cout<<"Case #"<<test<<":";
		for(long long i=0;i<s;++i)
			cout<<" "<<i*kk+1;

		cout<<"\n";
	}
} 