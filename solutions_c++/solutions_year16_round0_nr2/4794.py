#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>

using namespace std;

int main()
{
	/*freopen("B-large.in", "r", stdin);
	freopen("outB2.out", "w", stdout);*/

	int T;
	cin >> T;

	for(int i = 1; i <= T; ++i)
	{
		string S;
		int c = 0;
		cin >> S;
		for(int j = 0; j < S.length() - 1; ++j)
		{
			if(S[j] != S[j + 1])
				++c;
		}

		if(S.back() == '-')
			++c;

		cout << "Case #" << i << ": " << c << endl;
	}

	return 0;
}