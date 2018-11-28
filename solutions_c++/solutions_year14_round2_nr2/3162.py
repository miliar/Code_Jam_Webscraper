#include <iostream>
#include <iomanip>		// setprecision
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <map>			// map, unordered_map
#include <set>			// set, unordered_set
#include <algorithm>	// sort, stable_sort
#include <cstdlib>		// atoi, atof, etc.
#include <string>
using namespace std;

typedef unsigned long long ull_int;



ull_int F(ull_int A, ull_int B, ull_int K)
{	// A>=B
	if (K>=B)		return A*B;
	// A >= B > K
	ull_int res = K*(A +B - K);
	for (ull_int i=K; i<B; ++i)
		for (ull_int j=K; j<A; ++j)
		{
			if ( (i&j) < K)
				++res;
		}
	return res;
}


int main()
{
	ifstream infile;
	infile.open("B-small-attempt0.in");
	ofstream outfile;
	outfile.open("small.out");
	int nCases;

	infile >> nCases;
	for (int t=1; t<=nCases; t++)
	{
		int A, B, K;
		infile >> A >> B >> K;
				
		ull_int res = F(max(A,B), min(A,B), K);

		outfile << "Case #" << t << ": " << res << endl;
		cout << "Case #" << t << ": " << res << endl;			
	}
	infile.close();
	outfile.close();
	char c;
	cin >> c;
	return 0;
}