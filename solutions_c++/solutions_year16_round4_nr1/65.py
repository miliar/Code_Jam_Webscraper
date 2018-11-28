#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int data;
	scanf("%d", &data);
	for (int q = 1; q <= data; q++)
	{
		int num, r, p, c;
		scanf("%d%d%d%d", &num, &r, &p, &c);
		int n = 1 << num;
		bool flag = true;
		vector<string>rs, ps, cs;
		for (int i = 0; i < r; i++)rs.push_back("R");
		for (int i = 0; i < p; i++)ps.push_back("P");
		for (int i = 0; i < c; i++)cs.push_back("S");
		for (int j = 0; j < num; j++)
		{
			r = rs.size(), p = ps.size(), c = cs.size();
			n = r + c + p;
			if (r * 2 > n || p * 2 > n || c * 2 > n)
			{
				flag = false;
				break;
			}
			int rp = (r + p - c) / 2, pc = (-r + p + c) / 2, cr = (r - p + c) / 2;
			vector<string>nr, np, nc;
			for (int i = 0; i < rp; i++)
			{
				np.push_back(min(ps[0], rs[0]) + max(ps[0], rs[0]));
			}
			for (int i = 0; i < pc; i++)
			{
				nc.push_back(min(ps[0], cs[0]) + max(ps[0], cs[0]));
			}
			for (int i = 0; i < cr; i++)
			{
				nr.push_back(min(rs[0], cs[0]) + max(rs[0], cs[0]));
			}
			rs = nr, ps = np, cs = nc;
		}
		printf("Case #%d: ", q);
		if (!flag)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			if (!rs.empty())cout << rs[0] << endl;
			if (!ps.empty())cout << ps[0] << endl;
			if (!cs.empty())cout << cs[0] << endl;
		}
	}
}