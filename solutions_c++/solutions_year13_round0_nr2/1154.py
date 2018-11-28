// Problem B. Lawnmower

#include <algorithm>
#include <cassert>
#include <iostream>
using namespace std;

const unsigned N = 100;
static unsigned board[N][N];
static bool marked[N][N];
static unsigned X, Y;

static void markColumn(unsigned x)
{
	unsigned maximal = 0;
	for (unsigned y = 0; y < Y; ++y)
		maximal = max(maximal, board[x][y]);
	for (unsigned y = 0; y < Y; ++y)
		if (board[x][y] == maximal)
			marked[x][y] = true;
}

static void markRow(unsigned y)
{
	unsigned maximal = 0;
	for (unsigned x = 0; x < X; ++x)
		maximal = max(maximal, board[x][y]);
	for (unsigned x = 0; x < X; ++x)
		if (board[x][y] == maximal)
			marked[x][y] = true;
}

static bool allMarked()
{
	for (unsigned x = 0; x < X; ++x) {
		for (unsigned y = 0; y < Y; ++y) {
			if (!marked[x][y])
				return false;
		}
	}
	return true;
}

static const char* testcase()
{
	assert(cin);
	cin >> X >> Y;
	assert(cin);
	for (unsigned x = 0; x < X; ++x) {
		for (unsigned y = 0; y < Y; ++y) {
			cin >> board[x][y];
			marked[x][y] = false;
		}
	}
	assert(cin);

#if 0
	cout << '\n';
	for (unsigned x = 0; x < X; ++x) {
		for (unsigned y = 0; y < Y; ++y)
			cout << ' ' << board[x][y];
		cout << '\n';
	}
#endif

	for (unsigned x = 0; x < X; ++x)
		markColumn(x);
	for (unsigned y = 0; y < Y; ++y)
		markRow(y);

#if 0
	cout << '\n';
	for (unsigned x = 0; x < X; ++x) {
		for (unsigned y = 0; y < Y; ++y)
			cout << ' ' << marked[x][y];
		cout << '\n';
	}
#endif

	return allMarked() ? "YES" : "NO";
}

int main()
{
	unsigned n;
	cin >> n;
	assert(cin);
	for (unsigned i = 0; i < n; ++i)
		cout << "Case #" << i+1 << ": " << testcase() << '\n';
}
