// c.cpp
// Fair and Square
//

#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
using namespace std;

bool isFair(int n)
{
	stringstream ss;
	string s1, s2;
	ss << n;
	ss >> s1;
	s2 = s1;
	reverse(s2.begin(), s2.end());
	return ( s1 == s2 ? true : false );
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1 ; t <= T ; ++t) {
		// input
		int A, B;
		cin >> A >> B;

		int ans = 0;
		for (int n = A ; n <= B ; n++) {
			bool bFair, bSquare;

			// fair
			bFair = isFair(n);

			// square
			int rootn = sqrt((double)n);
			if (n == rootn * rootn && isFair(rootn))
				bSquare = true;
			else
				bSquare = false;


			if (bFair && bSquare)
				ans++;
		}

		// output
		if (t > 1)
			cout << endl;
		cout << "Case #" << t << ": " << ans;
	}

	return 0;
}