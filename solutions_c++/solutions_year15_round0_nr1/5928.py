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

long solve(long Smax, string& audience)
{
	long ans = 0;
	long sum_audience = 0;
	for (long i = 0; i <= Smax; i++)
	{
		char c = audience[i];
		long Si = atoi(&c);
		if (sum_audience + ans < i && Si!=0)
		{
			ans += i - (sum_audience+ans);
		}
		sum_audience += Si;
	}
	return ans;
}
int main()
{
	long T; cin >> T;
	vector<long> Smax(T);
	vector<string> audience(T);

	for (long i = 0; i < T; i++)
	{
		cin >> Smax[i] >> audience[i];
	}

	for (long i = 0; i < T; i++)
	{
		cout << "Case #" << (i+1) << ": " << solve(Smax[i], audience[i]) << endl;
	}

}
