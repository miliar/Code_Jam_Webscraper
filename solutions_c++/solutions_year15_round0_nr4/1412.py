#include <iostream>
#include <cstring>
using namespace std;

const string gab = "GABRIEL";
const string rich = "RICHARD";

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int X, R, C;
		cin >> X >> R >> C;

		if (R < C)
			swap(R, C);


		// R >= C
		string sol;
		switch (X) {
			case 1: 
				sol = gab;
				break;
			case 2:
				if ((R >= 2) && (R*C % 2 == 0))
					sol = gab;
				else
					sol = rich;
				break;
			case 3:
				if ((R == 3 && C == 2) || (R == 3 && C == 3) 
					|| (R == 4 && C == 3))
					sol = gab;
				else
					sol = rich;
				break;
			case 4:
				if ((R == 4 && C == 3) || (R == 4 && C == 4))
					sol = gab;
				else
					sol = rich;
				break;
		}


		cout << "Case #" << t << ": " << sol << endl;
	}


	return 0;
}