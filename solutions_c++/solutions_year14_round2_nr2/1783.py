#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long solve( long A, long B, long K )
{
	long num = 0;
	for (long i = 0; i < A; ++i)
		for (long j = 0; j < B; ++j)
			if ((i & j) < K)
				++num;
	return num;
}

int main()
{
	int nc = 0;
	cin >> nc;

	for (int c = 0; c < nc; ++c)
	{
		long A, B, K;
		cin >> A >> B >> K;

		int num = solve( A, B, K );

		cout << "Case #" << c + 1 << ": " << num << endl;
	}

	return 0;
}
