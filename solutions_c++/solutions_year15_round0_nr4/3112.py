#include <iostream>
#include <climits>
#include <complex>

using namespace std;

int main() {
	int N;
	cin >> N;
	
	int X,R,C;
//	while(cin >> X >> R >> C)
	for (int i = 0; i < N; i++)
	{
		cin >> X >> R >> C;
		//cout << (max(R,C) < X) << (((X/2)+1) > min(R,C) && X != 2) << (((R*C) % X) != 0) << endl;
		if ((max(R,C) < X) || (((X/2)+1) > min(R,C) && X != 2) || (((R*C) % X) != 0))
			cout << "Case #" << (i+1) << ": RICHARD" << endl;
		else
			cout << "Case #" << (i+1) << ": GABRIEL" << endl;
	}	
	return 0;
}
