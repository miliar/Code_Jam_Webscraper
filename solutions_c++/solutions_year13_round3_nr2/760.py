#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <set>
using namespace std;
typedef long long ll;
const long long MAX_LEN = 111111111;
const int SIZE = 201;
 int START;
string mas[SIZE][SIZE];
string ANS()
{
	int l, r;
	cin >> r >> l;
	return mas[l + START][r + START];
}
typedef pair<pair<int, int>, string> point;

int MAX_HOD = 270;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, - 1};
char DIRS[] = {'N', 'E', 'S', 'W'};
int COUNT1 = SIZE * SIZE;
int len = 0;
set<pair<pair<int, int>, int> > is_used;
void recalc()
{
	for (int i = 0; i < SIZE; i++)
		for (int j = 0; j < SIZE; j++)
		{
			mas[i][j] = "";
		}
	START = SIZE / 2;
	queue<pair<pair<int, int>, string> > qu;
	qu.push(make_pair(make_pair(0,0), ""));
	while(qu.empty() == false && COUNT1 > 0)
	{
		point pos = qu.front();
		qu.pop();

		int i = pos.first.first;
		int j = pos.first.second;
		if ((abs(i) <= SIZE / 2) && (abs(j) <= SIZE / 2) && (mas[i + START][j + START] == ""))
		{
			mas[i + START][j + START] = pos.second;
			COUNT1--;

			if (len != pos.second.size())
			{
				cerr <<"LEN : " << pos.second.size() << endl;
				cerr << COUNT1 << endl;
				len = pos.second.size();
			}
		}

		if ((abs(i) > MAX_HOD) || (abs(j) > MAX_HOD))
			continue;

		for (int dir = 0; dir < 4; dir++)
		{
			point new_point;

			new_point.second = pos.second;
			new_point.second.push_back(DIRS[dir]);
			new_point.first = pos.first;

			new_point.first.first += dx[dir] * (pos.second.size() + 1);
			new_point.first.second+= dy[dir] * (pos.second.size() + 1);

			pair<pair<int, int>, int> ppp;
			ppp.first = new_point.first;
			ppp.second = new_point.second.size();
			if (is_used.find(ppp) == is_used.end())
			{
				qu.push(new_point);
				is_used.insert(ppp);
			}
		}
	}
}
int main()
{
	recalc();
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int TESTS;
	cin >> TESTS;
	for (int TEST = 1; TEST <= TESTS; TEST++)
	{
		cout << "Case #" << TEST << ": " << ANS() << endl;
	}
	return 0;
}