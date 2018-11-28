#include <iostream>
#include <queue>
#include <list>
#include <algorithm>
#include <limits>
#include <functional>
#include <utility>
#include <vector>

using namespace std;

int makeMove(list<int> motes, long long A, int moves = 0)
{
	motes.sort();
	while(!motes.empty())
	{
		int lowestMote = motes.front();
		motes.pop_front();

		if(lowestMote < A)
		{
			// Standard situation
			A += lowestMote;
		}else
		{
			list<int> motesCopty(motes);
			// Special move needed
			int moves1 = makeMove(motes, A, moves + 1);
			int moves2 = numeric_limits<int>::max();

			long long possibleMote = A - 1;
			if(possibleMote > 0)
			{
				motesCopty.push_front(lowestMote);
				motesCopty.push_back(possibleMote);
				moves2 = makeMove(motesCopty, A, moves + 1);
			}

			return min(moves1, moves2);
		}
	}

	return moves;
}

int main()
{
	// Load cases
	int cases = 0;
	cin >> cases;

	for(int i = 0; i < cases; ++i)
	{
		list<int> motes;
		int mote;
		int N;
		long long A;
		cin >> A >> N;

		for(int j = 0; j < N; ++j)
		{
			cin >> mote;
			motes.push_back(mote);
		}
		// Calculate
		int moves = makeMove(motes, A);

		cout << "Case #" << (i + 1) << ": " << moves << endl;
	}
	return 0;
}
