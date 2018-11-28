#include <vector>
#include <list>
#include <map>
#include <set>
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

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");
	unsigned long long T, A,B,K;
	
	fin >> T;


	for (int i = 0; i < T; i++)
	{
		fout << "Case #" << i + 1 << ": ";
		int ans = 0, count = 0;
		fin >> A >> B >> K;


		for (int j = 0; j < A;j++)
		for (int k = 0; k < B; k++)
		{
			ans = j&k;
			if (ans < K)
				count++;

		}
		fout << count << endl;
	}

	return 0;
}