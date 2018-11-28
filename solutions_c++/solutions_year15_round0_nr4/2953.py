#include <iostream>
#include <vector>

using namespace std;

vector<int> v[5][5];

void init()
{
	// 1 x 1
	v[1][1].push_back(1);
	// 1 x 2
	v[1][2].push_back(1);
	v[1][2].push_back(2);
	// 1 x 3
	v[1][3].push_back(1);
	// 1 x 4
	v[1][4].push_back(1);
	v[1][4].push_back(2);

	// 2 x 1
	v[2][1].push_back(1);
	v[2][1].push_back(2);
	// 2 x 2
	v[2][2].push_back(1);
	v[2][2].push_back(2);
	// 2 x 3
	v[2][3].push_back(1);
	v[2][3].push_back(2);
	v[2][3].push_back(3);
	// 2 x 4
	v[2][4].push_back(1);
	v[2][4].push_back(2);
	
	// 3 x 1
	v[3][1].push_back(1);
	// 3 x 2
	v[3][2].push_back(1);
	v[3][2].push_back(2);
	v[3][2].push_back(3);
	// 3 x 3
	v[3][3].push_back(1);
	v[3][3].push_back(3);
	// 3 x 4
	v[3][4].push_back(1);
	v[3][4].push_back(2);
	v[3][4].push_back(3);
	v[3][4].push_back(4);
	
	// 4 x 1
	v[4][1].push_back(1);
	v[4][1].push_back(2);
	// 4 x 2
	v[4][2].push_back(1);
	v[4][2].push_back(2);
	// 4 x 3
	v[4][3].push_back(1);
	v[4][3].push_back(2);
	v[4][3].push_back(3);
	v[4][3].push_back(4);
	// 4 x 4
	v[4][4].push_back(1);
	v[4][4].push_back(2);
	v[4][4].push_back(4);
}

int main()
{
	init();

	int T;
	cin >> T;

	for(int t=1; t<=T; t++) 
	{
		int x, r, c;
		bool find = false;

		cin >> x >> r >> c;

		for(int i = 0; i < v[r][c].size(); i++) {
			if (v[r][c][i] == x) {
				find = true;
				break;
			}
		}

		cout << "Case #" << t << ": " << (find ? "GABRIEL" : "RICHARD") << endl;
	}

	return 0;
}
