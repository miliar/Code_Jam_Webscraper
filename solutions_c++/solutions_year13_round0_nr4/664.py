#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

class Solver
{
	struct Chest
	{
		int type;
		vector<int> keys;
		bool open;
	};

	int K, N, copen;
	map<int,int> myKeys;
	vector<Chest> chests;
	vector<int> steps;

	bool IsPossible() const
	{
		map<int, int> allKeys( myKeys );
		map<int, int> allTypes;
		map<int, int> selfRefs;

		for ( int i = 0; i < N; ++i )
		{
			auto & chest = chests[i];
			if ( chest.open )
				continue;
			++allTypes[chest.type];
			for ( int j = 0; j < chest.keys.size(); ++j ) {
				++allKeys[chest.keys[j]];
				if ( chest.keys[j] == chest.type )
					++selfRefs[chest.type];
			}
		}

		for ( auto it = allTypes.begin(); it != allTypes.end(); ++it ) {
			if ( it->second > allKeys[it->first] )
				return false;
			if ( allKeys[it->first] == selfRefs[it->first] && it->second == 1 )
				return false;
		}
		return true;
	}

	bool Step(int)
	{
		if ( copen == N ) {
			return true;
		}

		if ( !IsPossible() ) {
			return false;
		}

		map<int, int> myOrigKeys(myKeys);
		for ( int i = 0; i < N; ++i )
		{
			auto & chest = chests[i];
			if ( chest.open || !myKeys[chest.type] )
				continue;
			// Open chest
			--myKeys[chest.type];
			chest.open = true;
			for ( int j = 0; j < chest.keys.size(); ++j )
				++myKeys[chest.keys[j]];
			++copen;
			// Try
			if ( Step(i) ) {
				steps.push_back(i);
				return true;
			}
			// Close chest
			--copen;
			chest.open = false;
			myKeys = myOrigKeys;
		}
		return false;
	}

public:
	string Solve()
	{
		cin >> K >> N;
		
		int k;
		for ( int i = 0; i < K; ++i ) {
			cin >> k;
			++myKeys[k];
		}

		copen = 0;
		chests.resize(N);
		for ( int i = 0; i < N; ++i ) {
			cin >> chests[i].type;
			cin >> k;
			chests[i].keys.resize(k);
			for ( int j = 0; j < k; ++j ) {
				cin >> chests[i].keys[j];
			}
			chests[i].open = false;
		}


		if ( Step(-1) ) {
			stringstream ss;
			for ( auto it = steps.crbegin(); it != steps.crend(); ++it )
				ss << ' ' << (*it + 1);
			return ss.str().substr(1);
		} else
			return "IMPOSSIBLE";
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
