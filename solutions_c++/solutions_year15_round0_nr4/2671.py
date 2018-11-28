#include <iostream>
using namespace std;


int main() {
	int T;
	cin  >> T;

	for (int i=0;i<T;i++) {
		int X,R,C;

		cin >> X >> R >> C;

		string r;

		int a[4][4][4] = {
			{
				{1,1,1,1},
				{1,1,1,1},
				{1,1,1,1},
				{1,1,1,1}
			},
			{
				{0,1,0,1},
				{1,1,1,1},
				{0,1,0,1},
				{1,1,1,1}
			},
			{
				{0,0,0,0},
				{0,0,1,0},
				{0,1,1,1},
				{0,0,1,0}
			},
			{
				{0,0,0,0},
				{0,0,0,0},
				{0,0,0,1},
				{0,0,1,1},
			},

		};
		if (a[X-1][R-1][C-1]) {
			r = "GABRIEL";
		} else {
			r = "RICHARD";
		}

		cout << "Case #" << i + 1 << ": " << r << endl;
	}
	return 0;


}