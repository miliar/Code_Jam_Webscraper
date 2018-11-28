// b.cpp
// Lawnmower
//

#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1 ; t <= T ; t++) {
		const int MAXN = 100;
		const int MAXM = 100;
		int N, M;
		int lawn[MAXN][MAXM];
		bool able = true;

		// input
		cin >> N >> M;
		for (int r = 0 ; r < N ; r++)
		for (int c = 0 ; c < M ; c++)
			cin >> lawn[r][c];

		for (int r = 0 ; r < N ; r++) {
			for (int c = 0 ; c < M ; c++) {
				bool rable = true;
				bool cable = true;

				// row
				for (int i = 0 ; i < M ; i++)
					if (i != c && lawn[r][i] > lawn[r][c])
						rable = false;
				// col
				for (int i = 0 ; i < N ; i++)
					if (i != r && lawn[i][c] > lawn[r][c])
						cable = false;

				if (!rable && !cable) {
					able = false;
					break;
				}
			}
		}


		// output
		if (t > 1)
			cout << endl;
		cout << "Case #" << t << ": ";
		cout << (able ? "YES" : "NO");
	}

	return 0;
}