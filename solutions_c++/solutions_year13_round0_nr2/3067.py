#include <iostream>
#include <utility>
#include <vector>
using namespace std;

void testCase(int t)
{
	cout << "Case #" << t;
	
	int N, M;
	cin >> N >> M;
	
	// Read the pattern.
	
	int count = N*M;
	vector<short> _lawn;
	_lawn.reserve(count);
	short *lawn = _lawn.data();
	//short *lawn = new short[count];
	short *ptr = lawn;
	
	do
	{
		cin >> *ptr++;
	} while (--count);
	
	// Find the max values of each row and column.
	
	vector<short> rows(N, 0), cols(M, 0);
	
	ptr = lawn;
	for (int n = 0; n < N; ++n)
	{
		for (int m = 0; m < M; ++m)
		{
			rows[n] = max(rows[n], *ptr);
			cols[m] = max(cols[m], *ptr);
			++ptr;
		}
	}
	
	// Evaluate the possibility.
	ptr = lawn;
	for (int n = 0; n < N; ++n)
	{
		for (int m = 0; m < M; ++m)
		{
			if (*ptr < rows[n] && *ptr < cols[m])
			{
				cout << ": NO\n";
				return;
			}
			++ptr;
		}
	}
	
	cout << ": YES\n";
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	
	for (int i = 1; i <= T; ++i)
		testCase(i);
	
	return 0;
}