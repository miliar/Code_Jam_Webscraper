#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int w, h, b;

class Rect
{
public: 
	int x0, y0, x1, y1;
	Rect()
	{
		x0 = y0 = x1 = y1 = 0;
	}
	Rect(int a, int b, int c, int d)
		: x0(a)
		, y0(b)
		, x1(c)
		, y1(d)
		{}
};

Rect readRect()
{
	Rect tmp;
	cin >> tmp.x0 >> tmp.y0 >> tmp.x1 >> tmp.y1;
	return tmp;
}


vector <Rect> rects;

vector< vector< int > > dist;


int calcDist3(int x, int y, const Rect &r)
{
	if (r.x0 <= x && x <= r.x1) return min(abs(y-r.y0), abs(y-r.y1))-1;
	if (r.y0 <= y && y <= r.y1) return min(abs(x-r.x0), abs(x-r.x1))-1;
	int w = min(abs(x-r.x0), abs(x-r.x1));
	int h = min(abs(y-r.y0), abs(y-r.y1));
	return max(w, h)-1;
}


int calcDist2(const Rect &a, const Rect &b) {
	int ans = calcDist3(a.x0, a.y0, b);
	int cur;
	
	cur = calcDist3(a.x0, a.y1, b);
	if (cur < ans) ans = cur;

	cur = calcDist3(a.x1, a.y0, b);
	if (cur < ans) ans = cur;

	cur = calcDist3(a.x1, a.y1, b);
	if (cur < ans) ans = cur;

	if (ans < 0) ans = 0;

	return ans;
}

int calcDist(const Rect &a, const Rect &b) {
	int ans1 = calcDist2(a,b);
	int ans2 = calcDist2(b,a);
	return (ans1 < ans2 ? ans1 : ans2);
}

void Load()
{
	cin >> w >> h >> b;
	int i;
	dist.clear();
	rects.clear();
	rects.push_back(Rect(-1, -1, -1, h+1));
	for (i = 0; i < b; i++) {
		rects.push_back(readRect());
	}
	rects.push_back(Rect(w, -1, w, h+1));
	int j;
	b += 2;
	dist.resize(b);
	for (i = 0; i < b; i++) {
		dist[i].resize(b);
		for (j = 0; j < b; j++) {
			dist[i][j] = calcDist(rects[i], rects[j]);
			//cerr << i << ' ' << j << ' ' << dist[i][j] << "\n";
		}
	}
}




#define int64 long long

class Edge
{
public:
	int64 cost;
	int en;
};

const int64 MANY=0x7F7F7F7F7F7F7F7Fll;


int bver, ever;
int64 dst[51000];
int was[51000];
int nver;


void DijkstRA()
{
	memset(dst, 0x7F, sizeof(dst));
	memset(was, 0, sizeof(was));
	dst[bver] = 0;
	while (true)
	{
		int mi = -1;
		int j;
		for (j = 0; j < nver; j++)
			if (was[j] == 0 && (mi == -1 || dst[j] < dst[mi]))
				mi = j;
		if (mi == -1) break;
		was[mi] = 1;
		for (j = 0; j < nver; j++)
		{
			if (dst[j] > dst[mi] + dist[mi][j])
			{
				dst[j] = dst[mi] + dist[mi][j];
			}
		}
	}
}




void Solve()
{
	bver = 0;
	ever = b-1;
	nver = b;
	DijkstRA();
	cout << dst[b-1] << "\n";
}

int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
