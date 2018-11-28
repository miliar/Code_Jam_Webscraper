#include <iostream>
#include <vector>
#include <algorithm>
#include <future>

using namespace std;

int solve(vector<int> we)
{
	sort(we.begin(), we.end());
	int ret = we.back();
	for (int M = 2; M<we.back(); ++M)
	{
		int penalty = 0;
		auto we2(we);
		while (we2.back() > M)
		{
			auto t = we2.back();
			we2.back() = t - M;
			++penalty;
			sort(we2.begin(), we2.end());
		}
		we2.push_back(M);
		sort(we2.begin(), we2.end());
		ret = min(ret, we2.back() + penalty);
	}
	return ret;
}

int main()
{
	int T, D;
	cin >> T;
	vector<future<int>> f;
	for (int q = 1; q <= T; ++q)
	{
		cin >> D;
		vector<int> we(D);
		for (auto& i : we) cin >> i;
		f.push_back(async([we]{return solve(we); }));
	}
	for (int q = 1; q <= T; ++q) 
	{
		int ret = f[q - 1].get();
		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}