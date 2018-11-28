#include <iostream>

using namespace std;

int main()
{
	int t;
	string res = "GABRIEL";
	cin >> t;
	int x,r,c;
	for(int i = 1; i <= t; ++i)
	{
		res = "GABRIEL";
		cin >> x >> r >> c;
		if(r*c < x)
			res = "RICHARD";
		if(r*c % x != 0)
			res = "RICHARD";
		if(x == 4 and ((r == 2 and c == 4) or (c == 2 and r == 4)))
			res = "RICHARD";
		if(x == 4 and (r == 1 or c == 1))
			res = "RICHARD";
		if(x == 4 and (r == 2 or c == 2))
			res = "RICHARD";
		if(x == 3 and ((r == 1 and c == 3) or (c == 1 and r == 3)))
			res = "RICHARD";
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}