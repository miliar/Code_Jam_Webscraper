#include <bits/stdc++.h>
using namespace std;

int t;
long long n, x;
bool ok[10];

bool update(long long x);

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for(int k = 0; k < t; k++)
	{
		cin >> n;
		cout << "Case #" << k+1 << ": ";
		if(n == 0) 
		{
			cout << "INSOMNIA\n";
			continue;
		}
		x = n;
		memset(ok, 0, sizeof ok);
		while(!update(x))
		{
			x += n;
		}
		cout << x << "\n";
	}
	return 0;
}

bool update(long long x)
{
	while(x > 0)
	{
		ok[x % 10] = 1;
		x /= 10;
	}
	bool check = 1;
	for(int i = 0; i < 10; i++)
		check = check & ok[i];
	return check;
}