#include <bits/stdc++.h>

using namespace std;

signed main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++)
	{
		cout << "Case #" << z << ": ";
		int J, P, S, K;
		cin >> J >> P >> S >> K;
		vector<vector<int>> jps;
		for(int j = 1; j <= J; j++)
			for(int p = 1; p <= P; p++)
				for(int s = 1; s <= S; s++)
					jps.push_back({j, p, s});
		int msk_sz = 1 << jps.size();
		vector<vector<int>> ans;
		int jp[J + 1][P + 1], js[J + 1][S + 1], ps[P + 1][S + 1];
		memset(jp, 0, sizeof(jp));
		memset(js, 0, sizeof(js));
		memset(ps, 0, sizeof(ps));
		for(int msk = 1; msk < msk_sz; msk++)
		{
			if(__builtin_popcount(msk) <= ans.size())
				continue;
			bool ok = 1;
			for(int i = 0; ok && i < jps.size(); i++)
			{
				if((msk >> i) & 1)
				{
					ok &= (K >= ++jp[jps[i][0]][jps[i][1]]);
					ok &= (K >= ++js[jps[i][0]][jps[i][2]]);
					ok &= (K >= ++ps[jps[i][1]][jps[i][2]]);
				}
			}
			if(ok)
			{
				ans.clear();
				for(int i = 0; i < jps.size(); i++)
					if((msk >> i) & 1)
						ans.push_back(jps[i]);
			}
			memset(jp, 0, sizeof(jp));
			memset(js, 0, sizeof(js));
			memset(ps, 0, sizeof(ps));
		}
		cout << ans.size() << "\n";
		for(auto it: ans)
			cout << it[0] << ' ' << it[1] << ' ' << it[2] << "\n";
	}
	return 0;
}
