#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <iterator>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <cctype>

#define PRECISION 7
#define ARRAY_SIZE(a) sizeof(a)/sizeof(a[0])

using namespace std;

int main()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	unsigned int T;
	int A, B, K, i, j,result;
	int iter = 0;

	cin >> T;
	while (iter++ < T)
	{
		cin >> A >> B >> K;
		double C = (A >= B) ? A : B;
		double D = (C == A) ? B : A;
		result = 0;
		for (i = 0; i < C; ++i) {
			for (j = 0; j < D; ++j) {
				if((i&j) < K) result++;
			}
		}

		cout << "Case #" << iter << ": " << result << endl;
	}
	return EXIT_SUCCESS;
}