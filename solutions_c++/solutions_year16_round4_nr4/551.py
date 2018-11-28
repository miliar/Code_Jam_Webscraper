#include <bits/stdc++.h>

using namespace std;

bool valid(vector<vector<bool>> ops)
{
	for(int i = 0; i < ops.size(); ++i)
	{
		bool good = false;
		for(int j = 0; j < ops.size(); ++j)
		{
			if(ops[i][j])
			{
				good = true;

				vector<vector<bool>> nops = ops;
				nops.erase(nops.begin() + i);
				for(auto &r : nops)
					r.erase(r.begin() + j);

				if(!valid(nops))
					return false;
			}
		}
		if(!good)
			return false;
	}

	return true;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";

		int N;
		cin >> N;
		vector<vector<bool>> ops(N, vector<bool>(N));

		for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
		{
			char c;
			cin >> c;
			ops[i][j] = (c == '1');
		}

		int mini = 1000000000;
		for(int i = 0; i < 1 << (N * N); ++i)
		{
			auto nops = ops;

			bool good = true;
			int cnt = 0;

			for(int x = 0; x < N; ++x)
			for(int y = 0; y < N; ++y)
			{
				if(ops[x][y] && !(i & (1 << (x * N + y))))
					good = false;
				if(!ops[x][y] && (i & (1 << (x * N + y))))
				{
					nops[x][y] = true;
					cnt ++;
				}
			}

			//if(good)
			//	clog << "----- " << i << endl;

			if(good && valid(nops))
			{
				//clog << " ---- " << cnt << " " << bitset<9>(i) << endl;
				mini = min(mini, cnt);
			}
		}
		cout << mini << "\n";
	}
}
