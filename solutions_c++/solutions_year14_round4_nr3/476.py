#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <set>
using namespace std;

struct Rec
{
	int x0, x1, y0, y1;
};

struct mm
{
	int x, y, dir;
};

int u[1005][4005];

int main()
{
	int t;
	cin >> t;
	
	int move[4][2];
	move[0][0] = 0;
	move[0][1] = 1;
	move[1][0] = -1;
	move[1][1] = 0;
	move[2][0] = 0;
	move[2][1] = -1;
	move[3][0] = 1;
	move[3][1] = 0;

	for (int tt = 1; tt <= t; ++tt)
	{
		int w, h, b;
		cin >> w >> h >> b;
		
		Rec r;
		vector<Rec> rs;
		set<int> hh;
		map<int, int> m;
		hh.insert(0);
		hh.insert(h-1);
		
		for (int i = 0; i < b; ++i)
		{
			cin >> r.x0 >> r.y0 >> r.x1 >> r.y1;
			rs.push_back(r);
			if (r.y0 > 1)
				hh.insert(r.y0 - 1);
			hh.insert(r.y0);
			hh.insert(r.y1);
			if (r.y1 < h - 2)
				hh.insert(r.y1 + 1);
		}
		
//		int hc = 0;
//		for (set<int>::iterator it = hh.begin(); it != hh.end(); ++it)
//			m[*it] = hc++;

		int hc = h;		
		for (int i = 0; i < w; ++i)
			for (int j = 0; j < hc; ++j)
				u[i][j] = -1;
		for (int i = 0; i < b; ++i)
		{
			for (int j = rs[i].x0; j <= rs[i].x1; ++j)
//				for (int k = m[rs[i].y0]; k <= m[rs[i].y1]; ++k)
				for (int k = rs[i].y0; k <= rs[i].y1; ++k)
					u[j][k] = -2;
		}
		
		int res = 0;
		for (int id = 0; id < w; ++id)
		{
			mm pos;
			mm tmm;
			pos.x = id;
			pos.y = 0;
			pos.dir = 0;
			vector<mm> q;
			if (u[id][0] != -2)
				q.push_back(pos);
			while (q.size() > 0)
			{
				pos = q[q.size() - 1];
				q.pop_back();
				u[pos.x][pos.y] = -2;
//				cout << pos.x << " " << pos.y << endl;
				if (pos.y == hc-1)
				{
					res++;
					break;
				}
				for (int i = 3; i < 6; ++i)
				{
					tmm.dir = (pos.dir + i) % 4;
					tmm.x = pos.x + move[tmm.dir][0];
					tmm.y = pos.y + move[tmm.dir][1];
					if ((tmm.x < 0) || (tmm.x >= w) || (tmm.y < 0) || (tmm.y >= hc))
						continue;
					int tmp = u[tmm.x][tmm.y];
					if ((tmp != -2) && (tmp != id))
					{
						u[tmm.x][tmm.y] = id;
						q.push_back(tmm);
					}
				}
			}
		}
		
		cout << "Case #" << tt << ": " << res << endl;
	}

	return 0;
}
