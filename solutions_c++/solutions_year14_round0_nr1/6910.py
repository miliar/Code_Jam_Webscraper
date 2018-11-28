#define _CRT_SECURE_NO_DEPRECATE
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>
#include <complex>
using namespace std;

#define X first
#define Y second
#define pb push_back
#define mp make_pair

const double PI = acos(-1.0);
const int INF = 1e9;
const int MOD = 1e9 + 7;
const int M = INF;
const double RRR = 180.0 / PI;


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;





int main()
{

	freopen("INPUT.TXT", "r", stdin);
	freopen("OUTPUT.TXT","w",stdout);
	int t;
	cin >> t;
	int board1[5][5],board2[5][5];
	int r1, r2;
	vector<int> ans;
	int test = 1;
	while (t--)
	{
		cout << "Case #" << test << ": ";
		test++;
		ans.clear();
		cin >> r1;
		for (int i = 1; i <=4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				cin >> board1[i][j];
			}
		}
		cin >> r2;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				cin >> board2[i][j];
			}
		}
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				if (board1[r1][i] == board2[r2][j])
				{
					ans.push_back(board1[r1][i]);
				}
			}
		}
		if (ans.size() == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		if (ans.size() == 1)
		{
			cout << ans.back() << endl;
		}
		if (ans.size() > 1)
		{
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}