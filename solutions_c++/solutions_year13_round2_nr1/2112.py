#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <sstream>
#include <list>

using namespace std;

class Solver
{
	struct State
	{
		int A;
		list<int>::iterator head;
		list<int>::iterator tail;
		int depth;
	};
public:
	string Solve()
	{
		int A, N, m;
		list<int> motes;

		cin >> A >> N;
		for ( int i = 0; i < N; ++i ) {
			cin >> m;
			motes.push_back(m);
		}
		motes.sort();

		list<State> states;
		State start = { A, motes.begin(), motes.end(), 0 };
		states.push_back(start);

		while ( !states.empty() )
		{
			State state(states.front());
			states.pop_front();

			while ( state.head != state.tail && *state.head < state.A ) {
				state.A += *state.head++;
			}
			if ( state.head == state.tail )
			{
				stringstream ss;
				ss << state.depth;
				return ss.str();
			}

			++state.depth;

			State next1 = state;
			next1.A += state.A - 1;
			states.push_back(next1);

			State next2 = state;
			--next2.tail;
			states.push_back(next2);
		}
		return "WTF";
	}
};

int main()
{
	int T;
	cin >> T;
	for ( int t = 0; t < T; ++t )
	{
		cout << "Case #" << (t+1) << ": " << Solver().Solve() << endl;
	}
	return 0;
}
