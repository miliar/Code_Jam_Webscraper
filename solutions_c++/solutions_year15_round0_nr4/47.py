#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
	int tt;
	
	cin >> tt;
	for (int t = 1; t <= tt; ++t)
	{
		int x, r, c;
		cin >> x >> r >> c;
		
		string res = "RICHARD";
		if ((x <= 2) && ((r % x == 0) || (c % x == 0)))
			res = "GABRIEL";
		if ((x == 3) && (((r % 3 == 0) && (c > 1)) || ((c % 3 == 0) && (r > 1))))
			res = "GABRIEL";
		if ((x == 4) && (r > 2) && (c > 2) && ((r * c) % 4 == 0))
			res = "GABRIEL";
		if ((x == 5) && (r * c > 15) && ((r * c) % 5 == 0) && (r > 2) && (c > 2))
			res = "GABRIEL";
		if ((x == 6) && ((r * c) % 6 == 0) && (r > 3) && (c > 3))
			res = "GABRIEL";
		
		cout << "Case #" << t << ": " << res << endl;
	}

    return 0;
}
