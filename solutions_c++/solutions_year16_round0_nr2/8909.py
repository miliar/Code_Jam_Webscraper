#include<iostream>
#include<string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	string inp;
	for (int i=1; i<=t; i++)
	{
		cin >> inp;
		int start = 0, vals[inp.length()], len=0;
		if (inp[0] == '+')
			start = 1;
		vals[0] = 1;
		for (int j=1; j<inp.length(); j++)
		{
			if (inp[j-1] == inp[j])
			{
				vals[len]++;
			}
			else
			{
				len++;
				vals[len] = 1;
			}
		}
		len++;
		if ((start+len) % 2 == 0)
			len--;
		cout << "Case #" << i << ": " << len << endl;
	}
}
