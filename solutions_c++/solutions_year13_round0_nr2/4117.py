#ifdef DEBUG_OUTPUT
#include "debug_output.h"
#else
#define DEBUG(x)
#endif

#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
#include <cassert>
using namespace std;


// Enlarge MSVS stack size
#pragma comment(linker, "/STACK:16777216")

#define pb push_back
#define all(c) c.begin(), c.end()
#define mp(x, y) make_pair(x, y)
#define sz(x) static_cast<int>(x.size())
typedef long long int64;

typedef vector<vector<int>> vvi;
typedef vector<int> vi;

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

void initialize()
{
    freopen("_.in", "r", stdin);
    freopen("_.out", "w", stdout);
	std::ios_base::sync_with_stdio (false);
}

void input(vector<vector<int>>& board)
{
	int N, M;
	cin >> N >> M;

	board.resize(N, vector<int>(M,0));

	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
	{
		cin >> board[i][j];
	}
}

bool Can(vvi board)
{
	vvi res(board.size(), vi(board[0].size(), -1));

	for (int i = 0; i < board.size(); i++)
	{
		int max = board[i][0];
		for (int j = 0; j < board[0].size(); j++)
		{
			if (max < board[i][j])
				max = board[i][j];
		}

		for (int j = 0; j < board[0].size(); j++)
		{
			if (board[i][j] == max)
				res[i][j]++;
		}
	}


	for (int i = 0; i < board[0].size(); i++)
	{
		int max = board[0][i];
		for (int j = 0; j < board.size(); j++)
		{
			if (max < board[j][i])
				max = board[j][i];
		}

		for (int j = 0; j < board.size(); j++)
		{
			if (board[j][i] == max)
				res[j][i]++;
		}
	}

	for (int i = 0; i < board.size(); i++)
		for (int j = 0; j < board[0].size(); j++)
			if (res[i][j] < 0)
				return false;

	return true;
}

int main()
{
    initialize();

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++)
	{
		vector<vector<int>> board;
		input(board);

		bool can = Can(board);

		cout << "Case #" << i + 1 << ": " << (can ? "YES" : "NO") << endl;
	}

    
    return 0;
}
