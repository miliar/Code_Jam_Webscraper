#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;
typedef long long lli;




int main()
{
	int t;
	cin >> t;
	for (int j=1;j<=t;j++)
	{
		bool must_fit = true;

		int x,tr,r,tc,c;
		cin >> x >> tr >> tc;
		r = max(tr,tc);
		c = min(tr,tc);
		if (r*c % x != 0 ) must_fit = false;
		if (x > r) must_fit = false;
		if (x > 2*c) must_fit = false;
		if (x == 2*c && x>=4) must_fit = false;

		if (x==1) must_fit = true;
		cout << "Case #" << j;
		if (must_fit)
			printf(": GABRIEL\n");
		else printf(": RICHARD\n");
	}





	return 0;
}