#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef unsigned int u32;

int main()
{
	ifstream in("input.in");
	ofstream out("output.out");

	u32 T;
	in >> T;
	cout << "T=" << T << endl;
	++T;
	for (u32 i = 1; i < T; ++i)
	{
		u32 A, B, K;
		in >> A >> B >> K;
		cout << "A=" << A << " B=" << B << " K=" << K << endl;

		// brute force
		u32 result = 0;
		for (u32 j = 0; j < K; ++j)
			for (u32 m = 0; m < B; ++m)
				for (u32 n = 0; n < A; ++n)
				{
					if ((m & n) == j) { ++result; }
				}

		cout << "Case #" << i << ": " << result << endl;
		out << "Case #" << i << ": " << result << endl;
	}

	out.close();
	in.close();
	getchar();
	return 0;
}