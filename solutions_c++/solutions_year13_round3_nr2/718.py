/*
 * B.cpp
 *
 *  Created on: May 12, 2013
 *      Author: Mostafa Saad
 */

#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include<functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
#include<bitset>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)

typedef long long ll;

const double EPS = (1e-7);
int dcmp(double x, double y) {
	return fabs(x - y) <= EPS ? 0 : x < y ? -1 : 1;
}

#define pb					push_back
#define MP					make_pair
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;

string DIR = "NESW";
ll dx[4] = { 0, 1, 0, -1 };
ll dy[4] = { 1, 0, -1, 0 };

const int N = 5000;
const int OFF = N/2;
pair<char, pair<int, int> > grid[N][N];
bool vis[N][N];

string solve(int X, int Y) {

	clr(vis, 0);
	queue<pair<int, int> > q;
	q.push(make_pair(OFF, OFF));
	grid[OFF][OFF] = make_pair(-1, make_pair(-1, -1));
	vis[OFF][OFF] = 1;
	int dep = 1;

	while (!q.empty()) {
		int SZ = sz(q);
		lp(i, SZ) {
			int x = q.front().first - OFF;
			int y = q.front().second - OFF;
			q.pop();

			lp(d, 4) {
				int nx = x + dep * dx[d] + OFF;
				int ny = y + dep * dy[d] + OFF;

				if (nx < 0 || nx >= N)
					continue;
				if (ny < 0 || ny >= N)
					continue;
				if (vis[nx][ny])
					continue;

				grid[nx][ny] = make_pair(DIR[d], make_pair(x + OFF, y + OFF));
				vis[nx][ny] = 1;

				if (nx-OFF == X && ny-OFF == Y) {
					string ret = "";
					while (grid[nx][ny].first != -1) {
						ret += grid[nx][ny].first;
						x = grid[nx][ny].second.first;
						y = grid[nx][ny].second.second;
						nx = x;
						ny = y;
					}
					reverse(all(ret));
					return ret;
				}
				q.push(make_pair(nx, ny));
			}
		}
		/*

		 lp(i, n) {
		 lp(j, n)
		 {
		 if(grid[i][j] == -1)
		 cout<<"* ";
		 else
		 cout<<grid[i][j]<< " ";
		 }
		 cout << "\n";
		 }
		 cout << "*********************************\n";
		 */
		dep++;
	}

	cerr<<X<<" "<<Y<<"oooooh\n";
	assert(false);

	return "***!";\
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;
	lp(cc, cases)
	{
		int X, Y;
		cin>>X>>Y;

		cout<<"Case #"<<cc+1<<": "<<solve(X, Y)<<"\n";
	}

	return 0;
}
