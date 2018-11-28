#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

long long x[51][2];
const int OO = (int) 2e9;

#define cin fin
#define cout fout

int main()
{
	fstream fin("in.txt");
	fstream fout("out.txt");

	int T;
	int N;

	int input[1001];

	cin >> T;

	long long r1, r2;
	for (int t = 1; t <= T; t++)
	{
		r1 = r2 = 0;
		cin >> N;

		cin >> input[0];
		int maxdiff = 0;

		for (int i = 1; i < N; i++)
		{
			cin >> input[i];
			maxdiff = max(input[i - 1] - input[i], maxdiff);
		}

		// approach 1
		for (int i = 1; i < N; i++)
		{
			r1 += input[i]<input[i-1] ? input[i-1]-input[i] : 0;
		}

		// approach 2
		for (int i = 0; i < N-1; i++)
		{
			r2 += input[i]>maxdiff ? maxdiff : input[i];
		}
		cout << "Case #" << t << ": " << r1 << " " << r2 << endl;
	}

	fin.close();
	fout.close();

	return 0;
}