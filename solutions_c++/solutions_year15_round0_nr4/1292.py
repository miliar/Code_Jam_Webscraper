#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>

using namespace std;

struct building {
	int x0,x1,y1,y0;
};

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int x,r,c;
		cin >> x >> r >> c;

		if (r < c) {
			int temp = r;
			r = c;
			c = temp;
		}

		bool flag = true;
		if (x == 1) {
			flag = true;
		}
		else if (x > r) {
			flag = false;
		}
		else {
			if (x == 2) {
				bool poss[4][4] = {{false, false, false, false},
								   {true,  true,  false, false},
								   {false, true,  false, false},
								   {true,  true,  true,  true}};
				flag = poss[r-1][c-1];
			}
			else if (x == 3) {
				bool poss[4][4] = {{false, false, false, false},
								   {false, false, false, false},
								   {false, true,  true,  false},
								   {false, false, true,  false}};
				flag = poss[r-1][c-1];
			}
			else if (x == 4) {
				bool poss[4][4] = {{false, false, false, false},
								   {false, false, false, false},
								   {false, false, false, false},
								   {false, false, true,  true}};
				flag = poss[r-1][c-1];
			}
		}

		cout << "Case #" << (q + 1) << ": ";
		if (flag) cout << "GABRIEL" << endl;
		else cout << "RICHARD" << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}