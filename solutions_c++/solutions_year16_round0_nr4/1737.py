#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <set>
#include <string>
#include <iomanip>
 
using namespace std;

long long power(int a, int b)
{
	long long val = 1;

	for (int i = 1; i <= b; i++)
		val = val*a;

	return val;
}
 
int main()
{

	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {

		int K, C, S;
	
		cin >> K;
		cin >> C;
		cin >> S;	
	
		int numReqd;
		if (C == 1)
			numReqd = K;
		else {
			numReqd = K/2;
			if (K%2 == 1)
				numReqd++;
		}
	     cout << "Case #" << i+1 << ": ";
		if (S < numReqd) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (C == 1) {
			for (int j = 1; j <= K; j++)
				cout << j << " ";
			cout << endl;
			continue;
		}
		long long p = power(K, C-1);
		for (int j = 1; j+1 <= K; j=j+2)
				cout << ((j-1)*p) + (j+1) << " ";
		if (K%2 == 1)
			cout << (K-1)*p + 1;
		cout << endl;
	}

	return 0;
}

