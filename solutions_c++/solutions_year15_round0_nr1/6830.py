#include <iostream>
#include <string>
#include <fstream>
#define ll long long
using namespace std;

int main()
{
	fstream f("A-large.in");
	ofstream fo("A-large.out");
	ll n, size, sum;
	string s[10000];
	f >> n;
	for (ll j = 0; j < n; j++)
	{
		f >> size;
		f >> s[j];
	}
	for (ll j = 0; j < n; j++)
	{
		ll count = 0;
		sum  = s[j][0] - '0';
		for(int i = 1; i < s[j].length(); i++)
		{
			ll temp = s[j][i] - '0';
			if(i > sum)
			{
				count = count + (i - sum);
				sum = sum + temp + (i - sum);
			}
			else
				sum = sum + temp;
		}
		fo << "Case #" << j+1 << ": " << count << endl;
	}
	return 0;
}