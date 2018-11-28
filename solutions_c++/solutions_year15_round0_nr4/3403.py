#include <iostream>
#include <string>
using namespace std;

bool f(int X, int R, int C)
{
	switch(X)
	{
		case 1: return 1;
		case 2: return !(R & 1 && C & 1);
		case 3: return !(R * C % 3) && min(R, C) > 1;
		case 4:
		{
			if(min(R, C) < 4) return min(R, C) == 3 && !(max(R, C) & 3); // x & 3 == x % 4
			return !(R & 3 && C & 3);
		}
		default:
			return 0;
	}
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for(int u = 1; u <= T; ++u)
	{
		int X, R, C;
		cin >> X >> R >> C;
		
		string y = f(X, R, C) ? "GABRIEL" : "RICHARD";
		
		cout << "Case #" << u << ": " << y << endl;
	}
	return 0;
}