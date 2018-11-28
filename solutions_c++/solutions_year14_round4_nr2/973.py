#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <math.h>
#include <string>
#include <cstdio>

using namespace std;

int getMinIndex(vector<int>& A, int from, int to)
{
	int N = A.size();

	int minI = from;
	for (int i = from+1; i <= to; ++i)
	{
		if (A[i] < A[minI])
			minI = i;
	}
	return minI;
}

int swapToPos(vector<int>& A, int from, int to)
{
	int moves = abs(from-to);
	// Swap forward.
	if (from < to)
	{
		while (from < to)
		{
			swap(A[from], A[from+1]);
			from++;
		}
	}
	// Swap backwards.
	else
	{
		while (from > to)
		{
			swap(A[from], A[from-1]);
			from--;
		}
	}
	return moves;
}

int minSteps(vector<int>& A, int from, int to, vector<vector<int> >& memoria)
{
	if (from == to)
		return 0;

	if (memoria[from][to] != -1)
		return memoria[from][to];

	int N = A.size();
	int minI = getMinIndex(A, from, to);

	// Min to the left.
	int min1 = swapToPos(A, minI, from);
	min1 += minSteps(A, from+1, to, memoria);

	// Rollback.
	swapToPos(A, from, minI);

	// Min to the right.
	int min2 = swapToPos(A, minI, to);
	min2 += minSteps(A, from, to-1, memoria);

	//cout << "From: " << from << ", To: " << to << ", Min1 " << min1 << ", Min2 " << min2 << ", MinI: " << minI << endl;

	// Rollback.
	swapToPos(A, to, minI);

	memoria[from][to] = min(min1, min2);
	return memoria[from][to];
}

void solveCase(int t)
{
	int N;
	cin >> N;
	vector<int> A(N);
	for (int i = 0; i < N; ++i)
		cin >> A[i];

	vector<vector<int> > memoria = vector<vector<int> >(N, vector<int>(N, -1));
	cout << minSteps(A, 0, N-1, memoria);
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{	
		cout << "Case #" << t << ": ";
        solveCase(t);
        cout << endl;
	}
	
	return 0;
}