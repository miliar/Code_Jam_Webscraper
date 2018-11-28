#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;
typedef unsigned long long ull;

bool powOf2 (ull x)
{
	int cnt = 0;
	while (x % 2 == 0)
		x /= 2, cnt++;
	
	return x == 1;
}

int main()
{
	ull p, q;
	int t;
	cin >> t;
	for (int w = 0; w < t; ++w)
	{
		scanf ("%lld/%lld", &p, &q);
		cout << "Case #" << w+1 << ": ";
		
		if (not powOf2 (q))
			cout << "impossible" << endl;
		else
		{
			int cnt = 0;
			while (q % 2 == 0 and p < q)
				q /= 2, cnt++;
			cout << cnt << endl;
		}
	}
	
	return 0;
}	