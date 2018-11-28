#include <iostream>

using namespace std;

typedef long long llong;

int all = 0x03ff;

void fillIt(llong n, int &res)
{
	int d;
	while(n>0)
	{
		d = n%10;
		n = n/10;
		res = res | (1<<d);
	}
}

llong countIt(llong n)
{
	int res = 0;
	int i = 1;
	while(1)
	{
		fillIt(i*n, res);
		if(res==all)
			return i*n;
		i++;
	}
}

int main()
{
	// cout<< (1<<0) << endl;
	// return 0;
	int t;
	llong n;
	cin >> t;
	for(int i=1; i<=t; i++)
	{
		cin >> n;
		// n = i;
		if(n==0)
			cout<< "Case #" << i << ": INSOMNIA" << endl;
		else
		{
			cout<< "Case #" << i << ": " << countIt(n) << endl;
		}
	}
}