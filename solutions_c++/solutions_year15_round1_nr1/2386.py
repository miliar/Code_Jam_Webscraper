#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <bitset>
using namespace std;

long method1(vector<long>& M)
{
	long ans = 0;
	for (int i = 1; i < M.size(); ++i)
	{
		long sub = M[i - 1] - M[i];
		if (sub > 0)
		{
			ans += sub;
		}
	}
	return ans;
}

long method2(vector<long>& M)
{
	long max_sub = 0;
	long ans = 0;

	for (int i = 1; i < M.size(); ++i)
	{
		max_sub = max(max_sub, M[i - 1] - M[i]);
	}

	for (int i = 0; i < M.size() - 1; ++i)
	{
		if (M[i] < max_sub)
			ans += M[i];
		else
			ans += max_sub;
	}
	return ans;
}

int main()
{
	long T; cin >> T;
	vector<vector<long>> M(T);

	for (long i = 0; i < T; i++)
	{
		int N;	cin >> N;
		for (int j = 0; j <N; j++)
		{
			int k; cin >> k;
			M[i].push_back(k);
		}
	}
	for (int i = 0; i < T; ++i)
		cout << "Case #" << (i + 1) << ": " << method1(M[i]) <<" "<<method2(M[i]) << endl;

}
