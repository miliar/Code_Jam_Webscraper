#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve()
{
	string Ga = "GABRIEL";
	string Ri = "RICHARD";
	int X = 0, R = 0, C = 0;
	cin >> X >> R >> C;
	if (R <C)
	{
		int tmp = R;
		R = C;
		C = tmp;
	}
	if(R*C % X != 0)
		return Ri;
	if( C >= X)
		return Ga;
	if (R < X)
		return Ri;
	if (X < 3)
		return Ga;
	if (R*C == X)
		return Ri;
	if (C + C > X )
		return Ga;
	return Ri;
}

int main()
{
	int TC = 0;
	cin >> TC;
	for (int i = 0; i < TC; ++i)
	{
		string y = solve();
		cout << "Case #" << i + 1 << ": " << y << endl;
	}
	return 0;
}
