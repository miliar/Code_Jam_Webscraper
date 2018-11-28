#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

struct building {
	int x[2], y[2];
};

struct bevent {
	int x, y[2];
	int ins;

	inline bool operator < (const bevent& rhs) const {
		return x < rhs.x;
	}
};

int w, h, b;
building bd[1000];
bevent be[2000];

int y[8000], ycnt;

multiset<int> yes[1000];
vector<pair<int, int> > ye[1000];

struct edge {
	int x, y;
	int cap;
	edge(){}
	edge (int x, int y, int cap) : x(x), y(y), cap(cap) {}
};

int n, m;
vector<int> nodenum[1000];
edge e[1000000];
vector<int> elink[1000000];


int head, tail;
int queue[1000000], path[1000000], epath[1000000];
bool check[1000000];

int nf ()
{
	int res = 0;

	while (true) {
		head = tail = 0;
		path[0] = -1;
		queue[tail++] = 0;
		while (head<tail) {
			int x = queue[head++];

			for (int i=0; i<elink[x].size(); i++) {
				int y = e[elink[x][i]].y;
				int c = e[elink[x][i]].cap;

				if (c && !check[y]) {
					queue[tail] = y;
					epath[tail] = elink[x][i];
					path[tail++] = head-1;
					check[y] = true;

					if (y == n-1)
						break;
				}
			}
			if (check[n-1])
				break;
		}

		if (check[n-1]) {
			res++;

			for (int p = tail-1; p; p = path[p]) {
				int k = epath[p];
				e[k].cap--;
				e[k^1].cap++;
			}

			for (int i=0; i<tail; i++)
				check[queue[i]] = false;
		}

		else {
			memset (check, 0, sizeof(check));
			return res;
		}
	}
}


int overlap (pair<int, int> a, pair<int, int> b) { return 1; } // return min (a.second, b.second) - max(a.first, b.first) + 1; }
void makeedge (int a, int b, int cap)
{
	e[m++] = edge (a, b, cap);
	e[m++] = edge (b, a, 0);
	elink[a].push_back (m-2);
	elink[b].push_back (m-1);
}

int bsearch (int v)
{
	int low=0, high=ycnt, mid;
	while (low<=high) {
		mid = (low+high) / 2;
		if (y[mid] == v) return mid;
		if (y[mid] < v) low = mid+1;
		else high = mid-1;
	}
	return -1;
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {

		if (tt==10)
			tt=tt;

		scanf ("%d%d%d", &w, &h, &b);
		ycnt=0;
		for (int i=0; i<h; i++)
			y[ycnt++] = i;
		y[ycnt++] = 0;
		y[ycnt++] = h-1;
		for (int i=0; i<b; i++) {
			scanf ("%d%d%d%d", &bd[i].x[0], &bd[i].y[0], &bd[i].x[1], &bd[i].y[1]);
			y[ycnt++] = bd[i].y[0];
			y[ycnt++] = bd[i].y[1];
			if (bd[i].y[0]) y[ycnt++] = bd[i].y[0]-1;
			if (bd[i].y[1]+1 < h) y[ycnt++] = bd[i].y[1]+1;
		}
		sort (y, y+ycnt);
		ycnt = unique (y, y+ycnt) - y;
		for (int i=0; i<b; i++) {
			bd[i].y[0] = bsearch (bd[i].y[0]);
			bd[i].y[1] = bsearch (bd[i].y[1]);
		}

		for (int i=0; i<b; i++) {
			be[i].ins = 1;
			be[i].x = bd[i].x[0];
			be[i].y[0] = bd[i].y[0];
			be[i].y[1] = bd[i].y[1];

			be[b+i].ins = -1;
			be[b+i].x = bd[i].x[1]+1;
			be[b+i].y[0] = bd[i].y[0];
			be[b+i].y[1] = bd[i].y[1];
		}
		sort (be, be+b+b);

		int ptr=0;
		yes[0].clear ();
		for (int i=0; i<w; i++) {
			if (i) yes[i] = yes[i-1];
			while (ptr<b*2 && be[ptr].x == i) {
				if (be[ptr].ins == 1) {
					yes[i].insert (be[ptr].y[0]);
					yes[i].insert (be[ptr].y[1]);
				}
				else {
					multiset<int>::iterator it;
					it = yes[i].find (be[ptr].y[0]); yes[i].erase (it);
					it = yes[i].find (be[ptr].y[1]); yes[i].erase (it);
				}
				ptr++;
			}

			ye[i].clear ();
			
			int yl = 0;
			multiset<int>::iterator it = yes[i].begin ();
			while (it != yes[i].end()) {
				int y1 = *it;
				it++;
				int y2 = *it;
				it++;

				for (int j=yl; j<y1; j++)
					ye[i].push_back (make_pair (j, j));

				yl = y2+1;
			}

			for (int j=yl; j<ycnt; j++)
				ye[i].push_back (make_pair (j, j));

			/*
			int yl = 0;
			multiset<int>::iterator it = yes[i].begin ();
			while (it != yes[i].end()) {
				int y1 = *it;
				it++;
				int y2 = *it;
				it++;

				if (y1 != yl)
					ye[i].push_back (make_pair (yl, y1-1));

				yl = y2+1;
			}

			if (yl != ycnt)
				ye[i].push_back (make_pair (yl, ycnt-1));
				*/
		}

		n=m=0;
		elink[n].clear ();
		n++;

		for (int i=0; i<w; i++) {
			nodenum[i].clear ();
			for (int j=0; j<ye[i].size(); j++) {
				elink[n].clear ();
				nodenum[i].push_back (n++);
			}
		}

		for (int i=0; i<w; i++) {
			if (!ye[i].empty() && ye[i][0].first == 0)
				makeedge (0, nodenum[i][0], 1);
		}

		for (int i=1; i<n; i++) {
			elink[n+i].clear ();
			makeedge (i, i+n, 1);
		}
		n = n*2;

		elink[n].clear ();
		n++;

		for (int i=0; i<w; i++) {
			if (!ye[i].empty() && ye[i][ye[i].size()-1].second == ycnt - 1)
				makeedge (nodenum[i][ye[i].size()-1]+n/2, n-1, 1);
		}

		for (int i=0; i<w; i++) {
			for (int j=0; j+1<ye[i].size(); j++) {
				if (ye[i][j].second == ye[i][j+1].first - 1) {
					makeedge (nodenum[i][j+1]+n/2, nodenum[i][j], 1);
					makeedge (nodenum[i][j]+n/2, nodenum[i][j+1], 1);
				}
			}
		}

		for (int i=0; i<w-1; i++) {
			int p=0;
			for (int j=0; j<ye[i].size (); j++) {
				if (p) p--;
				while (p<ye[i+1].size() && ye[i+1][p].first <= ye[i][j].second) {
					if (ye[i+1][p].second >= ye[i][j].first) {
						makeedge (nodenum[i][j]+n/2, nodenum[i+1][p], overlap (ye[i][j], ye[i+1][p]));
						makeedge (nodenum[i+1][p]+n/2, nodenum[i][j], overlap (ye[i][j], ye[i+1][p]));
					}
					p++;
				}
			}
		}

		printf ("Case #%d: %d\n", ++tt, nf ());
		fprintf (stderr, "%d\n", tt);
	}

	return 0;
}
