// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const int MAXN = 2e5 + 123;
const int INF = MAXN;

char arr[200][200];
map <point, bool> mark;
bool impos = false;


map <point, set<char> > forbid;



int walk(point a, int r, int c)
{
	// cerr << "walking " << a.X << " " << a.Y << endl;
	point pos = a;
	char dir = arr[pos.X][pos.Y];
	if(arr[pos.X][pos.Y] == '.') return 0;
	while(!mark[pos])
	{
		if(arr[pos.X][pos.Y] != '.')
		{
			mark[pos] = true;
			dir = arr[pos.X][pos.Y];
		}

		// cerr << "POS " << pos.X << " " << pos.Y << "   d: " << dir << endl;

		if(dir == '^' && pos.Y - 1 < 0)
		{
			if(arr[pos.X][pos.Y] == '.') impos = true;
			arr[pos.X][pos.Y] = 'v';
			cerr << "pos " << pos.X << " " << pos.Y << " with d: " << dir << " change" << endl;
			return 1;
		}
		if(dir == 'v' && pos.Y + 1 >= r)
		{
			if(arr[pos.X][pos.Y] == '.') impos = true;
			arr[pos.X][pos.Y] = '^';
			cerr << "pos " << pos.X << " " << pos.Y << " with d: " << dir << " change" << endl;
			return 1;
		}

		if(dir == '>' && pos.X + 1 >= c)
		{
			if(arr[pos.X][pos.Y] == '.') impos = true;
			arr[pos.X][pos.Y] = '<';
			cerr << "pos " << pos.X << " " << pos.Y << " with d: " << dir << " change" << endl;
			return 1;
		}
		if(dir == '<' && pos.X - 1 < 0)
		{
			if(arr[pos.X][pos.Y] == '.') impos = true;
			arr[pos.X][pos.Y] = '>';
			cerr << "pos " << pos.X << " " << pos.Y << " with d: " << dir << " change" << endl;
			return 1;
		}

		if(dir == '<') pos.X += -1;
		if(dir == '>') pos.X +=  1;
		if(dir == '^') pos.Y -= 1 ;
		if(dir == 'v') pos.Y +=  1;

	}
	return 0;
}


int check(int r, int c)
{
	int result = 0;
	for (int i = 0; i < r; ++i)
	{
		forbid[make_pair(i, 0)].insert('<');
		forbid[make_pair(i, c-1)].insert('>');
		if(arr[i][0] == '.'){
			int pos = 0 ;
			while(pos < c && arr[i][pos] == '.') pos++;
			if(pos < c) forbid[make_pair(i, pos)].insert('<');
		}
		if(arr[i][c-1] == '.'){
			int pos = c-1 ;
			while(pos >=0 && arr[i][pos] == '.') pos--;
			if(pos >= 0) forbid[make_pair(i, pos)].insert('>');
		}
		// result += ok(i, 0, r, c);
		// result += ok(i, c-1, r, c);
	}
	for (int i = 0; i < c; ++i)
	{
		forbid[make_pair(0, i)].insert('^');
		forbid[make_pair(r-1, i)].insert('v');
		if(arr[0][i] == '.'){
			int pos = 0 ;
			while(pos < r && arr[pos][i] == '.') pos++;
			if(pos < r) forbid[make_pair(pos, i)].insert('^');
		}
		if(arr[r-1][i] == '.'){
			int pos = r-1 ;
			while(pos >=0 && arr[pos][i] == '.') pos--;
			if(pos >= 0) forbid[make_pair(pos, i)].insert('v');
		}
		// result += ok(0, i, r, c);
		// result += ok(r-1, i, r, c);
	}

	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			if(arr[i][j] != '.' && forbid[make_pair(i, j)].size() == 4){ impos = true;
				// cerr << "impos " << i << " " << j << endl;
			}
			if(forbid[make_pair(i, j)].find(arr[i][j]) != forbid[make_pair(i, j)].end()) result ++;
		}
	}

	return result;
}

int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		impos = false;
		forbid.clear();
		int result = 0;
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				cin >> arr[i][j];
			result = check(r, c);
			cout << "Case #" << test+1 << ": ";
			if(impos) cout << "IMPOSSIBLE" << endl;
			else cout << result << endl;
		}


		return 0;
	}