#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

int T, N, J;

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	ios::sync_with_stdio(0);

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> N >> J;
		cout << "Case #" << t << ": \n";
		
		int M = (N - 2) / 2;
		for (int i = 0; i < (1 << M) && J > 0; i++, J--)
		{
			cout << "1";
			for (int j = 0; j < M; j++)
			{
				if ((i&(1 << j)))
					cout << "11";
				else
					cout << "00";
			}
			cout << "1";
			for (int j = 3; j <= 11; j++)
				cout << " " << j;
			cout << "\n";
		}
	}

	return 0;
}