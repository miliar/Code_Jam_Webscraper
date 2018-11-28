#include<iostream>
#include<cstdint>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<iterator>
#include<string>

using namespace std;

pair<int64_t, int64_t> solve(vector<int64_t>& M)
{
	pair<int64_t, int64_t> r;
	r.first = 0;
	r.second = 0;

	if (M.empty()) return r;

	int64_t bb = M.at(0);
	int64_t md = 0;
	for (auto m : M)
	{
		r.first += bb > m ? bb - m : 0;
		md = max(md, bb - m);
		bb = m;
	}
	
	for (size_t i = 0; i < M.size() - 1;++i)
	{
		r.second += min(md, M.at(i));
	}

	return r;
}

int main()
{
	uint64_t T;
	cin >> T;

	for (uint64_t t = 0; t < T; ++t)
	{
		uint64_t N;
		cin >> N;
		vector<int64_t> M;
		for (int n = 0; n < N; ++n)
		{
			int64_t m;
			cin >> m;
			M.push_back(m);
		}

		auto s = solve(M);

		cout << "Case #" << t + 1 << ": " << s.first << " " << s.second << endl;
	}
	return 0;
}
